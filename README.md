# Home Price Prediction Web App

## Overview
This project is a full-stack web application that predicts home prices based on user inputs. The application leverages a machine learning model to provide accurate predictions and is designed with a user-friendly interface. It showcases skills in data science, machine learning, full-stack development, and cloud deployment.

## Features
- Predicts home prices using a Random Forest regression model trained on a dataset of 2,000,000 rows.
- User-friendly interface built with React and TypeScript for seamless interaction.
- Back-end API developed with Flask for data processing and prediction.
- Deployed on AWS Elastic Beanstalk with CloudFront integration for secure and efficient delivery.

## Technologies Used
### Front-End
- React.js
- TypeScript
- HTML/SCSS

### Back-End
- Flask
- Python

### Machine Learning
- RandomForestRegressor from scikit-learn

### Cloud Deployment
- AWS Elastic Beanstalk
- AWS S3
- AWS CloudFront

## Run locally
To run the application locally, follow these steps:
Note: Inside frontend-react HomePricePredictionForm ensure post request url is: http://127.0.0.1:5000/predict
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/home-price-prediction.git
   cd home-price-prediction
   ```

2. **Install Front-End Dependencies:**
   ```bash
   cd frontend-react
   npm install
   ```

3. **Install Back-End Dependencies:**
   ```bash
   cd backend-flask
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   - Start the back-end server:
     ```bash
     flask run
     ```
   - Start the front-end development server:
     ```bash
     npm start
     ```
## Run locally using Docker
Make sure docker is running
```
docker-compose up
```
## Usage
1. Open the application in your browser.
2. Enter the required details such as location, square footage, number of bedrooms, etc.
3. Click the "Predict" button to get an estimated home price.

## Model Performance
- **R² Score:** 0.788
- **RMSE:** $112,474
- **MAE:** $73,220

## Deployment
The application is hosted on AWS Elastic Beanstalk and optimized using CloudFront for enhanced performance.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For questions, please contact [tristansetha@gmail.com].

