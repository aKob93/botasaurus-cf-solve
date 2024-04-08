import subprocess
import os
from threading import Thread
import sys
import webbrowser
from .env import is_vmish
from .app import run_backend
from .port_kill_adapter import killfrontendandbackendports, killbackendport
def show_help():
    print("""
Botasaurus Server CLI

Options:
  --help  Show this message and exit.

Commands:
  (no arguments)    Runs both the backend and frontend services.
  backend           Runs only the backend api service.
  install           Installs the frontend service.
  dev               Run the backend normally, and the frontend in development mode with hot reloading, allowing you to see UI changes immediately as you update the Next.js frontend code in the "frontend/src" folder.  This functionality is mostly not needed and is only useful when you need to change frontend ui's appearance. 
""")

def open_browser():
    # Wait for a few seconds before opening the browser
    webbrowser.open('http://localhost:3000/')

def open_browser_in_thread():
    if not is_vmish:
        Thread(target=open_browser, daemon=True).start()

def install():
    print("Installing frontend dependencies...")
    frontend_dir = os.path.join(os.getcwd(), "frontend")
    subprocess.check_call("npm install && npm run build", shell=True, cwd=frontend_dir)

def print_frontend_run_message():
    print("Starting frontend server at http://localhost:3000/")

def start_frontend(is_dev):
    frontend_dir = os.path.join(os.getcwd(), "frontend")
    cmd = "npm run dev" if is_dev else "npm run start"
    result = subprocess.run(cmd, shell=True,
    stdout = None if is_dev else subprocess.DEVNULL,  # Suppress the standard output
    stderr= None if is_dev else subprocess.PIPE,  # Capture the standard error
    check=True,
    cwd=frontend_dir  # Return outputs as strings
)
    return result

def run_frontend(is_dev):
    try:
        start_frontend(is_dev)
    except subprocess.CalledProcessError as e:
        if e.stderr:
            print(e.stderr.decode('utf-8'))
        # Resolve Errors, When user forgets to install frontend
        install()
        print_frontend_run_message()
        open_browser_in_thread()
        start_frontend(is_dev)

def run_server():

    if len(sys.argv) == 1:
        print_frontend_run_message()
        killfrontendandbackendports()
        # No arguments provided, run both backend and frontend
        Thread(target=run_backend, daemon=True).start()
        open_browser_in_thread()
        run_frontend(False)
    elif "--help" in sys.argv:
        show_help()
    elif sys.argv[1] == "install":
        install()
    elif sys.argv[1] == "backend":
        # Argument "backend" provided, run only backend
        killbackendport()
        run_backend()
    elif sys.argv[1] == "dev":
        print_frontend_run_message()
        killfrontendandbackendports()
        # No arguments provided, run both backend and frontend
        Thread(target=run_backend, daemon=True).start()
        open_browser_in_thread()
        run_frontend(True)
    else:
        print(f"Error: No such command: {sys.argv[1]}")
        print("Try '--help' for help.")
        sys.exit(1) 