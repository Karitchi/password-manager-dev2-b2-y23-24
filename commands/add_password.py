from utils.json import read_credentials_from_json, write_credentials_to_json
from config import CREDENTIALS_FILE



def add_password(args):
    # Read existing credentials from file
    credentials = read_credentials_from_json(CREDENTIALS_FILE)

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
    write_credentials_to_json(CREDENTIALS_FILE, credentials)
    print(f"Added credentials for {args.username} at {args.service} successfully.")