import pickle
import numpy as np


from fitbitapi import getMaxHeartRate, getMaxHeartRateFake
import time
# Import the function from dbread.py
from dbutils import readFileContent
# Load the pre-trained CoPulse KNN machine learning model
# This model is stored in 'CoPulse-knnmodel.pkl' and loaded using pickle
filename = 'copulse-knnmodel.pkl'
model = pickle.load(open(filename, 'rb'))  # Load the model from the file system


def readFileAndCheckForHeartDisease(fileName):
    print(f"Reading File {fileName}!")
    maxHeartRate = getMaxHeartRate

    data = readFileContent(fileName, maxHeartRate)
    print(f"data={data}")
    my_prediction = model.predict(data)

    print(f"MyPrediction={my_prediction}")
    if my_prediction == 1:
        print("Need to alert the user now due to heart disease potential now.")

##        data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    # Now call the AI Model to figure out what condition your heart is in.

try:
    while True:
        print('Going to sleep 60 seconds')
        readFileAndCheckForHeartDisease('databaseUsers.txt')
        time.sleep(10)
        
except KeyboardInterrupt:
    print('Manual break by user')
except OtherThingWhichCanGoWrong:
    print('Other thing went wrong ... stopping!')


