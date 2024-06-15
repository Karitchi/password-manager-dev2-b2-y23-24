from commands import add_password, get_password, delete_password, list_credentials
from utils.parse_args import parse_args



def main():
    args = parse_args()

    if args.command == 'add':
        add_password.add_password(args)
        
    elif args.command == 'get':
        get_password.get_password(args.service)
        
    elif args.command == 'delete':
        delete_password.delete_password(args.service)
        
    elif args.command == 'list':
        list_credentials.list_credentials()

if __name__ == "__main__":
    main()
