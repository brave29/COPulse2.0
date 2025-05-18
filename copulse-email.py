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
import smtplib
from email.mime.text import MIMEText

subject = "CO-Pulse - Alert - WARNING THRESHOLD REACHED"
body = "Warning threshold detected, please exercise caution with your activity now."
sender = "copulseheartratemonitor@gmail.com"
recipients = ["jay.subra@gmail.com", "nereyaljay@gmail.com"]
password = "mjbs jxmy rafu esug"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
#    msg = body
    msg['Subject'] = subject
    msg['From'] = sender
    msg['Priority'] = "high"
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent with high!")


send_email(subject, body, sender, recipients, password)