import json
import os


def read_credentials_from_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}
    return data

# Function to write credentials to JSON file


def write_credentials_to_json(filename, credentials):
    with open(filename, 'w') as json_file:
        json.dump(credentials, json_file, indent=4)
