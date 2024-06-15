import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="CLI Password Manager")
    parser.add_argument('command', choices=[
                        'add', 'get', 'delete', 'list'], help="Action to perform")
    parser.add_argument('-s', '--service', help="Service or account name")
    parser.add_argument('-u', '--username', help="Username or login ID")
    parser.add_argument('-p', '--password', help="Password")

    return parser.parse_args()
