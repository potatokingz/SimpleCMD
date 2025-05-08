import os
import shutil
import datetime
import subprocess
import platform
import socket

def help_command():
    print("""
SimpleCMD Commands:

Basic File Operations:
  ls             List files
  cd [folder]    Change directory
  pwd            Show current folder
  mkdir [name]   Make a folder
  del [file]     Delete a file
  rmdir [name]   Delete a folder
  copy [src] [dst]  Copy a file
  move [src] [dst]  Move a file
  rename [old] [new] Rename a file

System Tools:
  clear          Clear the screen
  time           Show current date and time
  sysinfo        Show basic system info
  tasklist       Show running tasks
  whoami         Show your current username

Network Tools:
  ping [host]    Ping a server
  ipconfig       Show your IP address info
  tracert [host] Trace route to a host

Script Tools:
  run [file.py]  Run a Python script

General:
  help           Show this help message
  exit           Exit SimpleCMD
""")

# ==== BASIC ====
def ls_command(): print("\n".join(os.listdir()))
def cd_command(args): os.chdir(args[0]) if args else print("Usage: cd [folder]")
def pwd_command(): print(os.getcwd())
def clear_command(): os.system('cls' if os.name == 'nt' else 'clear')
def time_command(): print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
def mkdir_command(args): os.makedirs(args[0], exist_ok=True) if args else print("Usage: mkdir [name]")
def del_command(args): os.remove(args[0]) if args else print("Usage: del [file]")
def rmdir_command(args): shutil.rmtree(args[0]) if args else print("Usage: rmdir [name]")
def copy_command(args): shutil.copy(args[0], args[1]) if len(args) >= 2 else print("Usage: copy [src] [dst]")
def move_command(args): shutil.move(args[0], args[1]) if len(args) >= 2 else print("Usage: move [src] [dst]")
def rename_command(args): os.rename(args[0], args[1]) if len(args) >= 2 else print("Usage: rename [old] [new]")

# ==== SYSTEM INFO ====
def sysinfo_command():
    print("System:", platform.system(), platform.release())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())
    print("Hostname:", socket.gethostname())

def tasklist_command():
    os.system("tasklist" if os.name == "nt" else "ps aux")

def whoami_command():
    print("Current user:", os.getlogin())

# ==== NETWORK ====
def ping_command(args):
    if args:
        os.system(f"ping {args[0]}")
    else:
        print("Usage: ping [host]")

def ipconfig_command():
    os.system("ipconfig" if os.name == "nt" else "ifconfig")

def tracert_command(args):
    if args:
        os.system(f"tracert {args[0]}" if os.name == "nt" else f"traceroute {args[0]}")
    else:
        print("Usage: tracert [host]")

# ==== SCRIPT RUNNER ====
def run_command(args):
    if not args:
        print("Usage: run [filename.py]")
        return
    filename = args[0]
    if not filename.endswith(".py") or not os.path.exists(filename):
        print("Python file not found.")
        return
    os.system(f"python \"{filename}\"")

# ==== MAIN ====
def main():
    print("Welcome to SimpleCMD! Type 'help' for commands.")
    while True:
        try:
            raw = input(">>> ").strip()
            if not raw: continue
            parts = raw.split()
            cmd, args = parts[0], parts[1:]

            match cmd:
                case "help": help_command()
                case "ls": ls_command()
                case "cd": cd_command(args)
                case "pwd": pwd_command()
                case "clear": clear_command()
                case "time": time_command()
                case "mkdir": mkdir_command(args)
                case "del": del_command(args)
                case "rmdir": rmdir_command(args)
                case "copy": copy_command(args)
                case "move": move_command(args)
                case "rename": rename_command(args)
                case "sysinfo": sysinfo_command()
                case "tasklist": tasklist_command()
                case "whoami": whoami_command()
                case "ping": ping_command(args)
                case "ipconfig": ipconfig_command()
                case "tracert": tracert_command(args)
                case "run": run_command(args)
                case "exit":
                    print("Goodbye!")
                    break
                case _:
                    print(f"Unknown command: '{cmd}'. Try 'help'")
        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    main()
