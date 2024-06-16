from utils.parse_args import get_arguments
from password_manager import PasswordManager


def main():
    args = get_arguments()
    password_manager = PasswordManager(args)
    password_manager.run()


if __name__ == "__main__":
    main()
