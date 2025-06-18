# I have defined the main functions in this file to create a new user whose information needs to be hardcoded as args
# the args go are to be passed to the func create_user_payload() in the main() func at the end of this file

from dotenv import load_dotenv
import requests
import json
import os

def load_env_variables():
    '''loads env variables and returns a tuple (API_URL, USERNAME, PASSWORD)'''
    load_dotenv()

    API_URL = os.getenv("API_URL")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    if not all([API_URL, USERNAME, PASSWORD]):
        raise EnvironmentError("Missing one or more required environment variables - API_URL, USERNAME or PASSWORD")

    return (API_URL, USERNAME, PASSWORD)

def create_user_payload(name, full_name, given_name, family_name, email_address):
    '''returns a single user dictionary ready to be dumped into JSON'''
    user_payload = {
        "user": {
            "name": name,
            "fullName": full_name,
            "givenName": given_name,
            "familyName": family_name,
            "emailAddress": email_address
        }
    }

    return user_payload

def make_post_request(user_payload, api_url, username, password):
    '''returns None, makes API request, prints response statuses'''
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"    
    }

    full_name = user_payload["user"]["fullName"]
    
    try:
        response = requests.post(
            api_url,
            auth=(username, password),
            headers=headers,
            data=json.dumps(user_payload),
            timeout=15
        )

        if response.status_code == 201:
            print(f"User {full_name} created successfully.")
        elif response.status_code == 409:
            print(f"User {full_name} already exists.")
        else:
            print(f"Failed to create {full_name} with status code {response.status_code}")
            print(response.text)
    
    except Exception as e:
        print(f"Connection error occured creating user {full_name}.")
        print(f"Error: {e}")

def main():
    api_url, username, password = load_env_variables()
    user_payload = create_user_payload("john", "John Connor", "John", "Connor", "user@example.com")
    make_post_request(user_payload, api_url, username, password)

if __name__ == "__main__":
    main()