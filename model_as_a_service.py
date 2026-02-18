import json
import os
 
import requests
from dotenv import load_dotenv
 
load_dotenv()
 
 
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
 
 
# generating token for calling model
auth_base_url = (
    "https://daia.privatelink.azurewebsites.net/authentication-service/api/v1/auth"
)
path = "/generate-token"
input_data = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
response = requests.post(auth_base_url + path, json=input_data, verify=False)
print(json.dumps(response.json(), indent=4))
TOKEN = response.json()["token"]
 
# calling chat completion api
model_base_url = "https://daia.privatelink.azurewebsites.net/model-as-a-service"
path = "/chat/completions"
input_data = {
    # "model": "gpt-5",
    "model": "gpt-5",
    "messages": [{"role": "user", "content": "Tell me about Climate Change."}],
}
headers = {"Authorization": f"Bearer {TOKEN}"}
response = requests.post(
    model_base_url + path, json=input_data, headers=headers, verify=False
)
print(json.dumps(response.json(), indent=4))