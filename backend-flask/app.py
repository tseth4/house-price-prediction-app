from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the compressed model
model = joblib.load("model/house_price_model_v2_compressed.pkl")
scaler = joblib.load("model/scaler.pkl")  # Scaler used during training
zip_code_avg_price = pd.read_csv("model/zip_code_avg_price.csv", index_col=0) 
zip_code_avg_price = zip_code_avg_price.squeeze("columns")  # Explicitly squeeze columns

le = joblib.load("model/label_encoder.pkl")


# Home route
@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML file for user input

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from the form
        data = request.form
        
        
        # Encode state
        state = data['state']
        try:
            # Encode the state using LabelEncoder
            encoded_state = le.transform([state])[0]  
        except ValueError:
            return jsonify({'error': f"State '{state}' is not recognized. Please enter a valid state."})

        
        # Encode the zip code
        zip_code = float(data['zip_code'])  # Get the zip code input
        if zip_code in zip_code_avg_price.index:
            zip_code_encoded = zip_code_avg_price[zip_code]
        else:
            zip_code_encoded = zip_code_avg_price.mea
            
        # Prepare features
        numerical_features = np.array([
            float(data['bed']),
            float(data['bath']),
            float(data['acre_lot']),
            float(data['house_size']),
            zip_code_encoded
        ]).reshape(1, -1)  # Reshape to a single sample
        
        # Scale numerical features
        numerical_features_scaled = scaler.transform(numerical_features)

        # Combine scaled numerical features with encoded state
        features = np.hstack([numerical_features_scaled, [[encoded_state]]])

        # Make prediction
        prediction = model.predict(features)[0]

        # Return prediction as JSON
        return jsonify({
            'prediction': round(prediction, 2)  # Format the prediction nicely
        })
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
