# SimpleCMD

**SimpleCMD** is a command-line interface (CLI) tool written in Python. It emulates basic commands of the Windows Command Prompt (CMD), with a simple and user-friendly design. It supports commands for file management, system info, network diagnostics, and Python script execution. It also includes colorful output using `colorama` for better readability.

![SimpleCMD Banner](https://raw.githubusercontent.com/potatokingz/simplecmd/master/banner.png) *(Replace this link with your project image if needed)*

## Features

- **Basic file operations:**
  - `ls`, `cd`, `pwd`, `mkdir`, `del`, `rmdir`, etc.
  
- **System tools:**
  - `sysinfo` (show basic system info)
  - `tasklist` (show running tasks)
  - `whoami` (show current user)
  
- **Network tools:**
  - `ping` (ping a server)
  - `ipconfig` (show IP address info)
  - `tracert` (trace route to a host)
  
- **Run Python scripts** directly from the terminal using `run [file.py]`.

- **Clear screen** with the `clear` command.

- **Command and output** colored for better readability with `colorama`.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/potatokingz/simplecmd.git
   cd simplecmd
