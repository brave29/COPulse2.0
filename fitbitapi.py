# fitbitapi.py  
# Purpose: This script interacts with the Fitbit API to fetch a user's heart rate data.  
# Steps involved:  
# 1) Import necessary libraries.  
# 2) Define the Fitbit token and user authentication headers for secure API communication.  
# 3) Create a function getMaxHeartRate() that:  
#    - Makes an API request to Fitbit's intraday heart rate endpoint.  
#    - Parses the response data to determine the maximum heart rate for the day from the returned time-series data.  

# Import necessary libraries  
# requests: Used to make HTTP requests to external APIs  
# oauth2: Used for handling OAuth authentication (not explicitly implemented here)  
import requests  
import oauth2 as oauth2  

# Define the Fitbit token (authentication key) for secure API communication  
# This token authenticates requests made to the Fitbit API  
fitbit_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1BTRloiLCJzdWIiOiJCNVRSQ0YiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJyZXMgcmxvYyByd2VpIHJociBydGVtIiwiZXhwIjoxNzY0NTkzOTMxLCJpYXQiOjE3MzMwNTc5MzF9.zeMFyL_Bk36Sq27rX43IazEr89o6yA0uZFZIVMPCU9E"  

# Set the user ID for Fitbit API calls  
user_id = 'B5TRCF'  

# Create the authorization header using the token for API requests  
# This header will be sent along with the request to authenticate  
header = {'authorization': 'Bearer ' + fitbit_token}  


# Function to retrieve the maximum heart rate from the Fitbit API  
def getMaxHeartRate():  
    # Fetches the user's heart rate data from Fitbit's intraday heart rate API endpoint  
    # Parses the data to determine the maximum heart rate value observed during the intraday data interval.  
    # Returns: int - Maximum heart rate value observed during the data interval.  

    # Make a GET request to the Fitbit intraday heart rate endpoint  
    # This endpoint provides minute-by-minute heart rate data for the current day  
    response = requests.get(  
        "https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1min.json",  
        headers=header  
    )  

    # Print the HTTP response status code to verify successful communication  
    print('status code', response.status_code)  
    
    # Print the entire response JSON to debug or check the data structure  
    print(response.json())  
    
    # Extract heart rate data from the response  
    # 'activities-heart-intraday' contains time-series heart rate data  
    data = response.json()['activities-heart-intraday']['dataset']  

    # Initialize a variable to track the maximum heart rate  
    maxheartrate = 0  

    # Loop through the heart rate data to find the maximum value  
    for line in data:  
        if int(line['value']) > maxheartrate:  
            maxheartrate = int(line['value'])  

    # Return the maximum heart rate value  
    return maxheartrate  
