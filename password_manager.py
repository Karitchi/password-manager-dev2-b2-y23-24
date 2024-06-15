from config import CREDENTIALS_FILE
from utils import json


class PasswordManager:
    def __init__(self, args):
        self.stored_credentials = json.read_credentials_from_json(CREDENTIALS_FILE)
        self.args = args

    def run(self):
        if self.args.command == 'add':
            self.create_credentials(self.args, self.stored_credentials)
            
        elif self.args.command == 'get':
            self.fetch_credentials(self.args.service, self.stored_credentials)
            
        elif self.args.command == 'delete':
            self.remove_credential(self.args.service, self.stored_credentials)
            
        elif self.args.command == 'list':
            self.list_credentials(self.stored_credentials)

    def create_credentials(self, args, credentials):
        # Read existing credentials from file

        # Add new credentials
        new_credentials = {
            "username": args.username,
            "password": args.password
        }

    
        if args.service in credentials:
            for credential in credentials[args.service]:
                if credential['username'] == args.username:
                    print(f"Credentials for {args.username} already exist at {args.service}.")
                    return

            credentials[args.service].append(new_credentials)
        else:
            credentials[args.service] = [new_credentials]

        # Write updated credentials back to file
        json.write_credentials_to_json(CREDENTIALS_FILE, credentials)
        print(f"Added credentials for {args.username} at {args.service} successfully.")

    def fetch_credentials(self, service, credentials):
        # Read existing credentials from file

        if service in credentials:
            print(f"The credentials for service '{service}' are:")
            for credential in credentials[service]:
                print(f"\nPassword: {credential['password']}\nUsername: {credential['username']}")

        else:
            print(f"No credentials found for service '{service}'")

    def remove_credential(self, service, credentials):
        # Read existing credentials from file

        if service in credentials:
            credentials.pop(service)
            json.write_credentials_to_json(CREDENTIALS_FILE, credentials)
            print(f"Deleted credentials for service '{service}' successfully.")
        else:
            print(f"No credentials found for service '{service}'")

    def list_credentials(self, credentials):

        if not credentials:
            print("No credentials found.")
            return

        print("Your credentials are:")
        
        for service in credentials:
            print(f"\nService: {service}\n")
            for credential in credentials[service]:
                print(f"    Username: {credential['username']}\n    Password: {credential['password']}\n")