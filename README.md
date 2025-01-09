# House Price Prediction Web Application

This is a Flask-based web application that predicts house prices based on input features like the number of bedrooms, bathrooms, size in square feet, and location. The prediction is made using a trained Linear Regression model, and the input features are scaled for better performance.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Installation Instructions](#installation-instructions)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Model Training](#model-training)
7. [License](#license)

## Project Overview
This web application allows users to input the following house features:

- **Size** (in square feet)
- **Number of Bedrooms**
- **Number of Bathrooms**
- **Location** (Urban, Suburban, or Rural)

The model uses these features to predict the price of the house. The prediction is powered by a Linear Regression model trained on an open-source housing price dataset. The application scales the features using `StandardScaler` to ensure that the model works with consistent data.

## Technologies Used
- **Flask**: Web framework for Python.
- **scikit-learn**: Machine learning library used for training the Linear Regression model and scaling the features.
- **joblib**: Used for saving and loading the model and scaler.
- **HTML/CSS**: For building the front-end of the application.
- **Jinja2**: For rendering HTML templates in Flask.

## Installation Instructions

To run the application locally, follow the steps below:

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
Clone the repository to your local machine using the following command:

``` bash
git clone https://github.com/Aniket12xfe/House_Price_Predication.git
```
### Step 2: Create a Virtual Environment (Optional but Recommended)
To create a virtual environment, use the following commands:

```bash
python -m venv venv
```

### Activate the virtual environment:

- Windows:

``` bash
venv\Scripts\activate
```

- MacOS/Linux:

``` bash
source venv/bin/activate
```

### Step 3: Install Dependencies
Install the required dependencies using pip:

``` bash
pip install -r requirements.txt
```

You can generate the requirements.txt file by running:

``` bash
pip freeze > requirements.txt
``` 
### Step 4: Run the Application
Run the Flask app using the following command:

``` bash
python app.py
```
The app will be available at http://127.0.0.1:5000.

## Usage

Once the application is running, follow these steps:

Open a browser and navigate to http://127.0.0.1:5000.

### Fill in the form with the house features:
- **Size** (in square feet): The size of the house.
- **Number of Bedrooms**: The number of bedrooms.
- **Number of Bathrooms**: The number of bathrooms.
- **Location**: Choose one of the locations (Urban, Suburban, or Rural).

Click the "Predict Price" button to see the predicted house price.

The result will display the predicted price of the house.

## Project Structure

The project directory is structured as follows:

### Code Structure

```
house-price-prediction/
├── app.py                   # Main Flask application file
├── model/                   # Directory to store model and scaler
│   ├── house_price_model.joblib   # Trained machine learning model
│   ├── scaler.joblib        # Feature scaler used for scaling input data
├── static/                  # Static files (CSS, images)
│   └── styles.css           # Optional CSS for styling
├── templates/               # HTML templates
│   ├── index.html           # Home page with the form
│   └── result.html          # Page to display the predicted house price
├── requirements.txt         # List of Python dependencies
└── README.md                # This file
```

## Model Training

The model used in this application is a Linear Regression model trained on an open-source housing price dataset. 

The features used for training are:

- **Area** (in square feet)
- **Number of Bedrooms**
- **Number of Bathrooms**
- **Location** (encoded as Urban, Suburban, or Rural)

The features are scaled using `StandardScaler` to ensure consistency in the data for the model prediction. The model and scaler are saved using joblib and loaded in the Flask application for real-time predictions.

## Model Training Script

The model is trained using the following steps:

- Data preparation and feature selection.
- Splitting the data into training and testing sets.
Scaling the features.
- Training the Linear Regression model.
- Saving the trained model and scaler using joblib.
- The model and scaler are loaded in the Flask app for making predictions based on user input.

## Output Snapshot

Below is an example of the application's output after submitting house features:

### Input Form
![Input Form](https://github.com/Aniket12xfe/House_Price_Predication/blob/main/SnapShots/House%20Price%20Prediction%20-%20Brave%2008-01-2025%2022_34_12.png)

### Predicted Price
![Predicted Price](https://github.com/Aniket12xfe/House_Price_Predication/blob/main/SnapShots/House%20Price%20Prediction%20-%20Brave%2008-01-2025%2022_34_45.png)


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- [Aniket Chaudhari](https://github.com/Aniket12xfe)

