import json
import requests

BASE_URL = "http://localhost:4000"
ACCESS_TOKEN = "ctfd_90631aa454cb79553da3032f5f1aa1a4645070ee7a4a3b62972095ec2d8579a9"

# API endpoint
api_endpoint = "/api/v1/users?view=admin"
url = f"{BASE_URL}{api_endpoint}"

# Headers
headers = {
    "Authorization": f"Token {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

try:
    # Send the POST request
    response = requests.get(url, headers=headers)

    # Raise an exception for bad status codes (4xx or 5xx)
    response.raise_for_status()

    # Print the response
    print(f"Status Code: {response.status_code}")
    try:
        print("Response JSON:")
        print(json.dumps(response.json(), indent=4))
    except json.JSONDecodeError:
        print("Response Content (not JSON):")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"Status Code: {e.response.status_code}")
        print(f"Response Text: {e.response.text}")

