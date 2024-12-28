from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS

# Initialize Flask app
application = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
CORS(application, resources={r"/*": {"origins": "https://tseth4.github.io/house-price-prediction-app/"}})

# Load the compressed model and supporting files
model = joblib.load("model/house_price_model_v2_compressed.pkl")
scaler = joblib.load("model/scaler.pkl")  # Scaler used during training
zip_code_avg_price = pd.read_csv("model/zip_code_avg_price.csv", index_col=0).squeeze("columns")  # Load as Series
le = joblib.load("model/label_encoder.pkl")



@application.route('/')
def home():
    return "Welcome to the Home Page"
  
@application.route('/health')
def health():
    return "OK", 200

@application.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse incoming JSON data
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided. Ensure the request is JSON.'}), 400

        # Log received data
        print(f"Received data: {data}")

        # Encode state
        state = data.get('state', '')
        try:
            encoded_state = le.transform([state])[0]
        except ValueError:
            return jsonify({'error': f"State '{state}' not recognized. Available states: {list(le.classes_)}"}), 400

        # Encode zip code
        zip_code = float(data.get('zip_code', 0))
        zip_code_encoded = zip_code_avg_price.get(zip_code, zip_code_avg_price.mean())

        # Prepare numerical features
        numerical_features = np.array([
            float(data.get('bed', 0)),
            float(data.get('bath', 0)),
            float(data.get('acre_lot', 0)),
            float(data.get('house_size', 0)),
            zip_code_encoded
        ]).reshape(1, -1)

        # Scale numerical features
        numerical_features_scaled = scaler.transform(numerical_features)
        print(f"Scaled features: {numerical_features_scaled}")

        # Combine scaled features with encoded state
        features = np.hstack([numerical_features_scaled, [[encoded_state]]])

        # Make prediction
        prediction = model.predict(features)[0]

        # Return formatted prediction
        return jsonify({'prediction': round(prediction, 2)})

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
