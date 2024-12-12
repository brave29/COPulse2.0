# main.py
# Purpose: This script runs the heart disease detection logic by combining machine learning with user input.
# Steps involved:
# 1) Import required libraries.
# 2) Load the CoPulse KNN model file from the filesystem using the pickle library.
# 3) Retrieve user input via HTML forms and Fitbit API data.
# 4) If the user selects the "digital twin" option, fetch the heart rate in real-time via the Fitbit API using the getMaxHeartRate() method.
# 5) Predict the likelihood of heart disease using the pre-trained machine learning model.

# Import the getMaxHeartRate function from the fitbitapi module
# This function interacts with the Fitbit API to get real-time heart rate data.
from fitbitapi import getMaxHeartRate

# Import necessary components from Flask
# Flask: Framework for building web applications
# render_template: Used to dynamically generate HTML pages
# request: Handles user data submitted via HTTP
from flask import Flask, render_template, request

# Import required libraries
# pickle: Used to save/load machine learning models and other data
# numpy: Used for efficient number handling and mathematical operations
import pickle
import numpy as np

# Load the pre-trained CoPulse KNN machine learning model
# This model is stored in 'CoPulse-knnmodel.pkl' and loaded using pickle
filename = 'CoPulse-knnmodel.pkl'
model = pickle.load(open(filename, 'rb'))  # Load the model from the file system

# Initialize the Flask web application
app = Flask(__name__)


# Route for the home page
# This is the first page users see when they visit the application
@app.route('/')
def home():
    return render_template('main.html')  # Render the 'main.html' template


# Route for the prediction page
# Handles user interaction for predicting heart disease risk
# Accepts both GET and POST HTTP methods
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # Variable to store the calculated heart rate
    my_heartrate = 0

    # Handle form submission only when the request method is POST
    if request.method == 'POST':
        # Retrieve whether the user selected the 'digital twin' option from the submitted form
        digitaltwin = request.form.get('digitaltwin')
        
        # If the user selected 'Yes' for digital twin, use the Fitbit API to get real-time heart rate
        if digitaltwin == "Yes":
            thalach = getMaxHeartRate()
            my_heartrate = thalach  # Update heart rate value from Fitbit API

        # Retrieve general input from the form provided by the user
        age = int(request.form['age'])  # Convert age to an integer
        sex = request.form.get('sex')
        cp = request.form.get('cp')
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = request.form.get('fbs')
        restecg = int(request.form['restecg'])

        # If the user did NOT choose the digital twin, use the manually entered heart rate value
        if digitaltwin == "No":
            thalach = int(request.form['thalach'])

        # Collect additional health-related inputs from the user
        exang = request.form.get('exang')
        oldpeak = float(request.form['oldpeak'])
        slope = request.form.get('slope')
        ca = int(request.form['ca'])
        thal = request.form.get('thal')
        
        # Combine all user input into a format suitable for prediction
        # Reshape the data into a 2D numpy array
        data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        # Use the pre-trained machine learning model to predict the result
        my_prediction = model.predict(data)

        # Render the 'result.html' page with prediction and heart rate
        return render_template('result.html', prediction=my_prediction, heartrate=my_heartrate)


# Run the web application server
# This ensures that the web app starts when the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)