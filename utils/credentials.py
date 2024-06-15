from utils import json

def load(CREDENTIALS_FILE):
  return json.read_credentials_from_json(CREDENTIALS_FILE)