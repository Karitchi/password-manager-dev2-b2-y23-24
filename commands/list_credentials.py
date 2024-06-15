from utils.json import read_credentials_from_json
from config import CREDENTIALS_FILE

def list_credentials():
    credentials = read_credentials_from_json(CREDENTIALS_FILE)

    if not credentials:
        print("No credentials found.")
        return

    print("Your credentials are:")
    
    for service in credentials:
        print(f"\nService: {service}\n")
        for credential in credentials[service]:
            print(f"    Username: {credential['username']}\n    Password: {credential['password']}\n")