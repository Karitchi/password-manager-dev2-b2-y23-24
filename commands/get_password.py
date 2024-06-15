from utils import json
from config import CREDENTIALS_FILE

def get_password(service):
    # Read existing credentials from file
    credentials = json.read_credentials_from_json(CREDENTIALS_FILE)

    if service in credentials:
        print(f"The credentials for service '{service}' are:")
        for credential in credentials[service]:
            print(f"\nPassword: {credential['password']}\nUsername: {credential['username']}")

    else:
        print(f"No credentials found for service '{service}'")