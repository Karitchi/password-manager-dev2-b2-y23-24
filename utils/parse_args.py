import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="CLI Password Manager")
    subparsers = parser.add_subparsers(
        dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new credential')
    add_parser.add_argument(
        '-s', '--service', required=True, help='Service or account name')
    add_parser.add_argument(
        '-u', '--username', required=True, help='Username or login ID for the service')
    add_parser.add_argument(
        '-p', '--password', required=True, help='Password for the service')

    # Get command
    get_parser = subparsers.add_parser('get', help='Get a credential')
    get_parser.add_argument(
        '-s', '--service', required=True, help='Service or account name')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a credential')
    delete_parser.add_argument(
        '-s', '--service', required=True, help='Service or account name')

    # List command
    list_parser = subparsers.add_parser('list', help='List all credentials')

    # Interactive command
    interactive_parser = subparsers.add_parser(
        'interactive', help='Start interactive mode')

    return parser.parse_args()
