from config import CREDENTIALS_FILE
from utils import json
import getpass


class PasswordManager:
    def __init__(self, args):
        self.stored_credentials = json.read_credentials_from_json(
            CREDENTIALS_FILE)
        self.args = args

    def run(self):
        if self.args.command == 'add':
            self.add_credentials(self.args, self.stored_credentials)

        elif self.args.command == 'get':
            self.get_credentials(self.args.service, self.stored_credentials)

        elif self.args.command == 'delete':
            self.delete_credential(self.args.service, self.stored_credentials)

        elif self.args.command == 'list':
            self.list_credentials(self.stored_credentials)

        elif self.args.command == 'interactive':
            self.interactive(self.stored_credentials)

    def add_credentials(self, args, credentials):
        # Read existing credentials from file

        # Add new credentials
        new_credentials = {
            "username": args.username,
            "password": args.password
        }

        if args.service in credentials:
            for credential in credentials[args.service]:
                if credential['username'] == args.username:
                    print(
                        f"Credentials for {args.username} already exist at {args.service}.")
                    return

            credentials[args.service].append(new_credentials)
        else:
            credentials[args.service] = [new_credentials]

        # Write updated credentials back to file
        json.write_credentials_to_json(CREDENTIALS_FILE, credentials)
        print(
            f"Added credentials for {args.username} at {args.service} successfully.")

    def get_credentials(self, service, credentials):
        # Read existing credentials from file

        if service in credentials:
            print(f"The credentials for service '{service}' are:\n")
            for credential in credentials[service]:
                print(
                    f"    Username: {credential['username']}\n    Password: {credential['password']}\n")

        else:
            print(f"No credentials found for service '{service}'")

    def delete_credential(self, service, credentials):
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
                print(
                    f"    Username: {credential['username']}\n    Password: {credential['password']}\n")

    def interactive(self, credentials):
        print("Welcome to the interactive mode of the password manager.")
        print("Enter 'exit' to quit the program.")
        while True:
            command = input(
                "Enter a command (add, get, delete, list): ").strip()

            if command == 'exit':
                break

            elif command == 'add':

                self.args.service = input("Enter the service name: ")
                self.args.username = input("Enter the username: ")
                self.args.password = getpass.getpass(
                    prompt="Enter the password: ")

                self.add_credentials(self.args, credentials)

            elif command == 'get':
                self.args.service = input("Enter the service name: ")

                self.get_credentials(self.args.service, credentials)

            elif command == 'delete':
                self.args.service = input("Enter the service name: ")

                self.delete_credential(self.args.service, credentials)

            elif command == 'list':
                self.list_credentials(credentials)

            else:
                print("Invalid command. Please try again.")
