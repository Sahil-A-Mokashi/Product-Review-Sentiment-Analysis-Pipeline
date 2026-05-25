import requests
from google.auth import default,exceptions
import google.auth
import google.auth.transport.requests

def get_my_session():
    try:
        creds, project = google.auth.default()
        auth_req = google.auth.transport.requests.Request()
        creds.refresh(auth_req)
        session = requests.Session()
        print("token for session created",str(creds.token)[:4])
        session.headers.update({'Authorization':f'Bearer {creds.token}'})
        print("authenticated session created")
        return session
    except Exception as e:
        print("error getting the default credentials",e)
        return None

def get_access_token():
    try:
        creds, project = google.auth.default()
        auth_req = google.auth.transport.requests.Request()
        creds.refresh(auth_req)
        print("token for session created",str(creds.token)[:4])
        return str(creds.token)
    except Exception as e:
        print("error getting the default credentials",e)
        return None