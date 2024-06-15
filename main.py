from utils.parse_args import parse_args
from password_manager import PasswordManager

def main():
    args = parse_args()
    password_manager = PasswordManager(args)
    password_manager.run()

if __name__ == "__main__":
    main()
