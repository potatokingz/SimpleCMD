import os
import shutil
import datetime
import subprocess
import platform
import socket
from colorama import init, Fore, Style

init(autoreset=True)

def c(text, color):
    return getattr(Fore, color.upper()) + text + Style.RESET_ALL

def banner():
    print(c("""
 ________  ___  _____ ______   ________  ___       _______           ________  _____ ______   ________     
|\   ____\|\  \|\   _ \  _   \|\   __  \|\  \     |\  ___ \         |\   ____\|\   _ \  _   \|\   ___ \    
\ \  \___|\ \  \ \  \\\__\ \  \ \  \|\  \ \  \    \ \   __/|        \ \  \___|\ \  \\\__\ \  \ \  \_|\ \   
 \ \_____  \ \  \ \  \\|__| \  \ \   ____\ \  \    \ \  \_|/__       \ \  \    \ \  \\|__| \  \ \  \ \\ \  
  \|____|\  \ \  \ \  \    \ \  \ \  \___|\ \  \____\ \  \_|\ \       \ \  \____\ \  \    \ \  \ \  \_\\ \ 
    ____\_\  \ \__\ \__\    \ \__\ \__\    \ \_______\ \_______\       \ \_______\ \__\    \ \__\ \_______\
   |\_________\|__|\|__|     \|__|\|__|     \|_______|\|_______|        \|_______|\|__|     \|__|\|_______|
   \|_________|                                                                                             
                                                                                                           
""", "cyan"))

def help_command():
    print(c("SimpleCMD Commands:\n", "cyan"))
    
    print(c("Basic File Operations:", "yellow"))
    print("  ls             List files")
    print("  cd [folder]    Change directory")
    print("  pwd            Show current folder")
    print("  mkdir [name]   Make a folder")
    print("  del [file]     Delete a file")
    print("  rmdir [name]   Delete a folder")
    print("  copy [src] [dst]  Copy a file")
    print("  move [src] [dst]  Move a file")
    print("  rename [old] [new] Rename a file")
    
    print(c("\nSystem Tools:", "yellow"))
    print("  clear          Clear the screen")
    print("  time           Show current date and time")
    print("  sysinfo        Show basic system info")
    print("  tasklist       Show running tasks")
    print("  whoami         Show your current username")
    
    print(c("\nNetwork Tools:", "yellow"))
    print("  ping [host]    Ping a server")
    print("  ipconfig       Show your IP address info")
    print("  tracert [host] Trace route to a host")
    
    print(c("\nScript Tools:", "yellow"))
    print("  run [file.py]  Run a Python script")
    
    print(c("\nGeneral:", "yellow"))
    print("  help           Show this help message")
    print("  exit           Exit SimpleCMD")

def success(msg): print(c(msg, "green"))
def error(msg): print(c("Error: " + msg, "red"))
def info(msg): print(c(msg, "cyan"))

def ls_command(): print("\n".join(os.listdir()))
def cd_command(args): os.chdir(args[0]) if args else error("Usage: cd [folder]")
def pwd_command(): print(os.getcwd())
def clear_command(): os.system('cls' if os.name == 'nt' else 'clear')
def time_command(): print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
def mkdir_command(args): os.makedirs(args[0], exist_ok=True) if args else error("Usage: mkdir [name]")
def del_command(args): os.remove(args[0]) if args else error("Usage: del [file]")
def rmdir_command(args): shutil.rmtree(args[0]) if args else error("Usage: rmdir [name]")
def copy_command(args): shutil.copy(args[0], args[1]) if len(args) >= 2 else error("Usage: copy [src] [dst]")
def move_command(args): shutil.move(args[0], args[1]) if len(args) >= 2 else error("Usage: move [src] [dst]")
def rename_command(args): os.rename(args[0], args[1]) if len(args) >= 2 else error("Usage: rename [old] [new]")

def sysinfo_command():
    print("System:", platform.system(), platform.release())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())
    print("Hostname:", socket.gethostname())

def tasklist_command():
    os.system("tasklist" if os.name == "nt" else "ps aux")

def whoami_command():
    print("Current user:", os.getlogin())

def ping_command(args): os.system(f"ping {args[0]}") if args else error("Usage: ping [host]")
def ipconfig_command(): os.system("ipconfig" if os.name == "nt" else "ifconfig")
def tracert_command(args): os.system(f"tracert {args[0]}" if os.name == "nt" else f"traceroute {args[0]}") if args else error("Usage: tracert [host]")

def run_command(args):
    if not args:
        error("Usage: run [filename.py]")
        return
    filename = args[0]
    if not filename.endswith(".py") or not os.path.exists(filename):
        error("Python file not found.")
        return
    os.system(f"python \"{filename}\"")

def main():
    clear_command()
    banner()
    info("Welcome to SimpleCMD! Type 'help' for commands.")
    while True:
        try:
            raw = input(c(">>> ", "magenta")).strip()
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
                    info("Goodbye!")
                    break
                case _: error(f"Unknown command: '{cmd}'. Try 'help'")
        except Exception as e:
            error(str(e))

if __name__ == "__main__":
    main()
