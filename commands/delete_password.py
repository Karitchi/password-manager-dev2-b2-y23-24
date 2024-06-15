from utils.json import read_credentials_from_json, write_credentials_to_json
from config import CREDENTIALS_FILE

def delete_password(service):
    # Read existing credentials from file
    credentials = read_credentials_from_json(CREDENTIALS_FILE)

    if service in credentials:
        credentials.pop(service)
        write_credentials_to_json(CREDENTIALS_FILE, credentials)
        print(f"Deleted credentials for service '{service}' successfully.")
    else:
        print(f"No credentials found for service '{service}'")