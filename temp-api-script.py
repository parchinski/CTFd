import json
import os
import requests

BASE_URL = "http://127.0.0.1:4000"
ACCESS_TOKEN = "ctfd_90631aa454cb79553da3032f5f1aa1a4645070ee7a4a3b62972095ec2d8579a9"
FILE_NAME = "users.csv"

# API endpoint
api_endpoint = "/api/v1/exports/raw"
url = f"{BASE_URL}{api_endpoint}"

# Headers
headers = {
    "Authorization": f"Token {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

# payload
payload = {"type": "csv", "args": {"table": "users"}}

try:
    # Send the POST request with JSON payload
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    # Raise an exception for bad status codes (4xx or 5xx)
    response.raise_for_status()

    # Handle the file download response
    print(f"Status Code: {response.status_code}")

    safe_filename = os.path.basename(FILE_NAME)  # Basic safety
    save_path = os.path.join(".", safe_filename)  # Save in current directory

    with open(save_path, "wb") as f:
        f.write(response.content)
    print(f"Successfully downloaded and saved file as: {save_path}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    if hasattr(e, "response") and e.response is not None:
        print(f"Status Code: {e.response.status_code}")
        print(f"Response Text: {e.response.text}")
