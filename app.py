from flask import Flask, render_template, request
from joblib import load
import numpy as np

app = Flask(__name__)

# Load the trained Linear Regression model
model = load('model/linear_regression_model.joblib')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Extract input features from the form
    area = int(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    stories = int(request.form['stories'])
    mainroad = 1 if request.form['mainroad'] == 'yes' else 0
    guestroom = 1 if request.form['guestroom'] == 'yes' else 0
    basement = 1 if request.form['basement'] == 'yes' else 0
    hotwaterheating = 1 if request.form['hotwaterheating'] == 'yes' else 0
    airconditioning = 1 if request.form['airconditioning'] == 'yes' else 0
    parking = int(request.form['parking'])
    prefarea = 1 if request.form['prefarea'] == 'yes' else 0

    # Combine features into a single array
    features = [area, bedrooms, bathrooms, stories, mainroad, guestroom, basement,
                hotwaterheating, airconditioning, parking, prefarea]

    # Predict the house price
    prediction = model.predict([features])[0]

    return render_template('result.html', price=round(prediction, 2))


if __name__ == '__main__':
    app.run(debug=True)
