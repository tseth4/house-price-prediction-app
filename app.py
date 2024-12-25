from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and scaler
model = joblib.load('house_price_model_v1.pkl')
scaler = joblib.load('scaler.pkl')

# Numerical features used during training
numerical_features = ['bed', 'bath', 'acre_lot', 'house_size', 'zip_code_encoded']

def preprocess_input(data):
    """
    Preprocess input data for the model.
    :param data: Dictionary with raw input features
    :return: Processed DataFrame
    """
    input_df = pd.DataFrame([data])
    input_df[numerical_features] = scaler.transform(input_df[numerical_features])
    return input_df

@app.route('/')
def home():
    """Render the input form."""
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle form submission and make predictions."""
    try:
        # Parse input from form
        input_data = {
            'bed': float(request.form['bed']),
            'bath': float(request.form['bath']),
            'acre_lot': float(request.form['acre_lot']),
            'house_size': float(request.form['house_size']),
            'zip_code_encoded': float(request.form['zip_code_encoded'])
        }

        # Preprocess data and make prediction
        processed_data = preprocess_input(input_data)
        prediction = model.predict(processed_data)[0]

        return render_template('result.html', prediction=f"${prediction:,.2f}")

    except Exception as e:
        return render_template('result.html', prediction=f"Error: {e}")

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for predictions."""
    try:
        # Parse JSON input
        input_json = request.get_json()

        # Validate input
        required_fields = ['bed', 'bath', 'acre_lot', 'house_size', 'zip_code_encoded']
        for field in required_fields:
            if field not in input_json:
                return jsonify({'error': f'Missing field: {field}'}), 400

        # Preprocess data and make prediction
        processed_data = preprocess_input(input_json)
        prediction = model.predict(processed_data)[0]

        # Return prediction as JSON
        return jsonify({'prediction': f"${prediction:,.2f}"})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
