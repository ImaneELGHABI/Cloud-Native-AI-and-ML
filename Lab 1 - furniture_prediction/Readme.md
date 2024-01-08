

# Heart Disease Prediction Flask App

## Overview
This Flask web application predicts the likelihood of heart disease in patients using a Support Vector Machine (SVM) model trained on clinical parameters.

## Installation
```
git clone [repository-link]
cd [repository-name]
pip install -r requirements.txt
```

## Usage
To run the Flask application locally:
```
export FLASK_APP=app.py
flask run
```
Navigate to `http://127.0.0.1:8082/` in your web browser.

## Features
- Predict heart disease based on user input.
- Reset functionality for the input form.
- Predict button to submit the form and see the prediction.

## Model Information
- The `best_model_SVM.pkl` is the trained SVM model used for predictions.
- The model was trained on the `Heart_Disease_Prediction.csv` dataset.

## Endpoints
- `/` (GET): Renders the home page with the input form.
- `/predict` (POST): Takes input from the form and returns the prediction.

## Screenshots
### Application Home Page
![Application Home Page](https://cdn.discordapp.com/attachments/1191490101247758479/1193574906055634984/flask1.png)

### Prediction Results
![Prediction Results](https://cdn.discordapp.com/attachments/1191490101247758479/1193574906315685898/flask2.png)


## Deployment
For deployment on Heroku, We need credits.

