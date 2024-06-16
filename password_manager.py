from config import CREDENTIALS_FILE
from utils import json
import getpass


class PasswordManager:
    def __init__(self, args):
        self.credentials = json.read_credentials_from_json(CREDENTIALS_FILE)
        self.args = args

    def run(self):
        commands = {
            'add': self.add_credentials,
            'get': self.get_credentials,
            'delete': self.delete_credential,
            'list': self.list_credentials,
            'interactive': self.interactive_mode
        }

        command = self.args.command
        if command in commands:
            commands[command]()
        else:
            print(f"Unknown command: {command}")

    def add_credentials(self):
        service = self.args.service
        username = self.args.username
        password = self.args.password

        if not service or not username or not password:
            print("Service, username, and password are required to add credentials.")
            return

        if service in self.credentials:
            for credential in self.credentials[service]:
                if credential['username'] == username:
                    print(
                        f"Credentials for {username} already exist at {service}.")
                    return
            self.credentials[service].append(
                {"username": username, "password": password})
        else:
            self.credentials[service] = [
                {"username": username, "password": password}]

        json.write_credentials_to_json(CREDENTIALS_FILE, self.credentials)
        print(f"Added credentials for {username} at {service} successfully.")

    def get_credentials(self):
        service = self.args.service
        if not service:
            print("Service name is required to get credentials.")
            return

        if service in self.credentials:
            print(f"The credentials for service '{service}' are:\n")
            for credential in self.credentials[service]:
                print(
                    f"    Username: {credential['username']}\n    Password: {credential['password']}\n")
        else:
            print(f"No credentials found for service '{service}'")

    def delete_credential(self):
        service = self.args.service
        if not service:
            print("Service name is required to delete credentials.")
            return

        if service in self.credentials:
            self.credentials.pop(service)
            json.write_credentials_to_json(CREDENTIALS_FILE, self.credentials)
            print(f"Deleted credentials for service '{service}' successfully.")
        else:
            print(f"No credentials found for service '{service}'")

    def list_credentials(self):
        if not self.credentials:
            print("No credentials found.")
            return

        print("Your credentials are:")
        for service, creds in self.credentials.items():
            print(f"\nService: {service}\n")
            for credential in creds:
                print(
                    f"    Username: {credential['username']}\n    Password: {credential['password']}\n")

    def interactive_mode(self):
        print("Welcome to the interactive mode of the password manager.")
        print("Enter 'exit' to quit the program.")
        while True:
            command = input(
                "Enter a command (add, get, delete, list): ").strip()

            if command == 'exit':
                break

            if command not in ['add', 'get', 'delete', 'list']:
                print("Invalid command. Please try again.")
                continue

            if command == 'add':
                service = input("Enter the service name: ").strip()
                username = input("Enter the username: ").strip()
                password = getpass.getpass("Enter the password: ")
                self.args.service = service
                self.args.username = username
                self.args.password = password
                self.add_credentials()
            elif command == 'get':
                service = input("Enter the service name: ").strip()
                self.args.service = service
                self.get_credentials()
            elif command == 'delete':
                service = input("Enter the service name: ").strip()
                self.args.service = service
                self.delete_credential()
            else:
                self.list_credentials()
