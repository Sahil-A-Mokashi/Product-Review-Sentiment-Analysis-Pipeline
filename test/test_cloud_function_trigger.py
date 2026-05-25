import requests
import json
import authenticated_session

url = "https://us-central1-poc-analytics-ai.cloudfunctions.net/sentiment-analysis-public"
payload = json.dumps({
  "name": "Hello World"
})
token = authenticated_session.get_access_token()
headers = {
  'Authorization': f'bearer {token}',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)