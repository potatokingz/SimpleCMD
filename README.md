# SimpleCMD

SimpleCMD is a command-line interface (CLI) tool written in Python. It emulates basic commands of the Windows Command Prompt (CMD), with a simple and user-friendly design. It supports commands for file management, system info, network diagnostics, and Python script execution. It also includes colorful output using `colorama` for better readability.

## Features

### Basic file operations:
- `ls`, `cd`, `pwd`, `mkdir`, `del`, `rmdir`, etc.

### System tools:
- `sysinfo` (show basic system info)
- `tasklist` (show running tasks)
- `whoami` (show current user)

### Network tools:
- `ping` (ping a server)
- `ipconfig` (show IP address info)
- `tracert` (trace route to a host)

### Other features:
- Run Python scripts directly from the terminal using `run [file.py]`.
- Clear screen with the `clear` command.
- Command and output colored for better readability with `colorama`.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/potatokingz/simplecmd.git
    cd simplecmd
    ```

2. Install the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the `simplecmd.py` script:

    ```bash
    python simplecmd.py
    ```

2. Type a command and hit enter to execute it. Example commands:
    - `ls` – List files in the current directory
    - `cd [folder]` – Change to a specified folder
    - `ping [host]` – Ping a server or host
    - `run [file.py]` – Run a Python script

3. Type `help` to see all available commands.

4. Type `exit` to quit the program.

## Example Commands

### Basic file operations:
- `ls` – List files and directories
- `cd foldername` – Change to a directory
- `pwd` – Display the current working directory
- `mkdir new_folder` – Create a new directory
- `del file.txt` – Delete a file
- `rmdir foldername` – Delete a folder

### System tools:
- `sysinfo` – Display basic system information
- `tasklist` – Display a list of running tasks
- `whoami` – Show your current username

### Network tools:
- `ping www.example.com` – Ping a host
- `ipconfig` – Display IP configuration
- `tracert www.example.com` – Trace route to a host

## Dependencies
- Python 3.x
- `colorama` library for colored output

You can install the necessary dependencies by running:

```bash
pip install -r requirements.txt
