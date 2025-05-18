import requests

# Function to send a Pushover notification
def send_pushover_notification(message, title="Notification"):
    url = "https://api.pushover.net/1/messages.json"
    # Example Usage
    app_token = "a77r5u9tr3mxgp3s3m3xgbrst7t175"    # Replace with your app's API token
    user_key = "u44rz64w4j1fpdxn965r6g8bmwv9wq"      # Replace with your Pushover user key

    # Prepare the payload with necessary parameters
    payload = {
        "token": app_token,     # Your app's API token
        "user": user_key,       # Your user key
        "message": message,     # The message you want to send
        "title": title          # Title of the notification (optional)
    }

    # Send POST request to Pushover API
    response = requests.post(url, data=payload)
    
    # Check the response
    if response.status_code == 200:
        print("Notification sent!")
    else:
        print("Failed to send notification:", response.text)


