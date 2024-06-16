# Password Manager

## Description

This CLI Password Manager is a Python-based tool to manage your credentials. It provides functionalities to add, get, delete, list, and interactively manage your credentials.

## Features

- **Add Credentials**: Store new service credentials (service name, username, and password).
- **Get Credentials**: Retrieve stored credentials for a specific service.
- **Delete Credentials**: Remove credentials for a specific service.
- **List Credentials**: Display all stored credentials.
- **Interactive Mode**: Manage credentials interactively through the command line.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/password-manager.git
   cd password-manager
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line Arguments

The password manager can be used with the following commands:

- `add`: Add new credentials.
- `get`: Get credentials for a service.
- `delete`: Delete credentials for a service.
- `list`: List all credentials.
- `interactive`: Enter interactive mode to manage credentials.

### Adding Credentials

To add new credentials, use the `add` command with the required options:

```bash
python main.py add -s <service> -u <username> -p <password>
```

### Getting Credentials

To get credentials for a specific service, use the `get` command:

```bash
python main.py get -s <service>
```

### Deleting Credentials

To delete credentials for a specific service, use the `delete` command:

```bash
python main.py delete -s <service>
```

### Listing Credentials

To list all stored credentials, use the `list` command:

```bash
python main.py list
```

### Interactive Mode

To manage credentials interactively, use the `interactive` command:

```bash
python main.py interactive
```

## Configuration

The configuration file path is defined in `config.py`:

```python
CREDENTIALS_FILE = 'credentials.json'
```
