import json
from os import environ
 
import requests
 
CLIENT_ID = environ.get("CLIENT_ID")
CLIENT_SECRET = environ.get("CLIENT_SECRET")
 
 
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
    "model": "gpt-5",
    "messages": [{"role": "user", "content": "Hello, how are you?"}],
}
headers = {"Authorization": f"Bearer {TOKEN}"}
response = requests.post(
    model_base_url + path, json=input_data, headers=headers, verify=False
)
print(json.dumps(response.json(), indent=4))