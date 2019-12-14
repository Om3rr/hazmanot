import requests
from app import client
from config.google import GOOGLE_DISCOVERY_URL, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
import json
from google.oauth2 import id_token
from google.auth.transport import requests

def validate_with_token(token):
    request = requests.Request()

    return id_token.verify_oauth2_token(
        token, request, GOOGLE_CLIENT_ID)

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()



def get_google_user(request):
    google_provider_cfg = get_google_provider_cfg()
    code = request.args.get("code")
    token_endpoint = google_provider_cfg.get("token_endpoint")
    print(request.url)
    print(request.base_url)
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    token = client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = google_provider_cfg.get("userinfo_endpoint")
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
        return {
            "email": users_email,
            "profile_pic": picture,
            "username": users_name,
            "id_": unique_id,
            "google_token": json.dumps(token)
        }
    else:
        return None