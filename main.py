import os
import requests
import base64
from dotenv import load_dotenv

# Load .env file
load_dotenv()
# Configuration

API_KEY=os.getenv("API_KEY")


headers = {
    "Content-Type": "application/json",
}

# Payload for the request
payload = {
   	"messages": [
		{
			"role": "system",
			"content": "You are a mathematician"
		},
		{
			"role": "user",
			"content": "What is 1+1?"
		}
	]
}

ENDPOINT = "http://localhost:8000/chat-azure"

# Send request
try:
    response = requests.post(ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")

# Handle the response as needed (e.g., print or process)
print(response.json())
