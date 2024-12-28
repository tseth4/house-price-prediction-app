from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS
import logging

# Initialize Flask app
application = Flask(__name__)
CORS(application, resources={r"/*": {"origins": "*"}})

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variables for lazy loading
model = None
scaler = None
zip_code_avg_price = None
zip_code_avg_price_mean = None
state_map = None

def load_resources():
    """Lazy load ML model and supporting files."""
    global model, scaler, zip_code_avg_price, zip_code_avg_price_mean, state_map
    if model is None:
        logger.info("Loading model and supporting resources...")
        model = joblib.load("model/house_price_model_v2_compressed.pkl")
        scaler = joblib.load("model/scaler.pkl")
        zip_code_avg_price = pd.read_csv("model/zip_code_avg_price.csv", index_col=0).squeeze("columns")  # Load as Series
        zip_code_avg_price_mean = zip_code_avg_price.mean()  # Cache mean
        label_encoder = joblib.load("model/label_encoder.pkl")
        state_map = {state: idx for idx, state in enumerate(label_encoder.classes_)}  # Precompute state mapping
        logger.info("Resources loaded successfully.")

def encode_state(state):
    """Encode state using precomputed mapping."""
    return state_map.get(state, None)

@application.route('/')
def home():
    return "Welcome to the Home Page"

@application.route('/health')
def health():
    return "OK", 200

@application.route('/predict', methods=['POST'])
def predict():
    try:
        # Load resources only when prediction is called
        load_resources()

        # Parse incoming JSON data
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided. Ensure the request is JSON.'}), 400

        # Log received data
        logger.info(f"Received data: {data}")

        # Encode state
        state = data.get('state', '')
        encoded_state = encode_state(state)
        if encoded_state is None:
            return jsonify({'error': f"State '{state}' not recognized."}), 400

        # Encode zip code
        zip_code = float(data.get('zip_code', 0))
        zip_code_encoded = zip_code_avg_price.get(zip_code, zip_code_avg_price_mean)

        # Prepare numerical features
        numerical_features = np.array([
            data.get('bed', 0),
            data.get('bath', 0),
            data.get('acre_lot', 0),
            data.get('house_size', 0),
            zip_code_encoded
        ], dtype=np.float32).reshape(1, -1)

        # Scale numerical features
        numerical_features_scaled = (numerical_features - scaler.mean_) / scaler.scale_
        logger.info(f"Scaled features: {numerical_features_scaled}")

        # Combine scaled features with encoded state
        features = np.hstack([numerical_features_scaled, [[encoded_state]]])

        # Make prediction
        prediction = model.predict(features)[0]

        # Return formatted prediction
        return jsonify({'prediction': round(prediction, 2)})

    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logger.info("Preloading resources...")
    load_resources()  # Preload resources at startup
    application.run(host='0.0.0.0', port=5000)
