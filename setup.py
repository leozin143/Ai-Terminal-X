import subprocess
import sys
import os

# define required system and python packages
system_packages = ["tmux", "xfce4-terminal", "xclip"]
python_packages = ["google-generativeai", "python-dotenv"]

# scripts to make executable
scripts_to_make_executable = ["ai-terminal-x.py", "command_suggester.py"]

def install_system_packages():
    print("installing required system packages...")
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y"] + system_packages, check=True)
        print("system packages installed successfully.")
    except subprocess.CalledProcessError:
        print("failed to install system packages. make sure you're using a debian-based system and have sudo access.")

def install_python_packages():
    print("installing required python packages...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install"] + python_packages, check=True)
        print("python packages installed successfully.")
    except subprocess.CalledProcessError:
        print("failed to install python packages.")

def make_scripts_executable():
    print("setting executable permission for scripts...")
    for script in scripts_to_make_executable:
        if os.path.exists(script):
            try:
                subprocess.run(["chmod", "+x", script], check=True)
                print(f"{script} is now executable.")
            except subprocess.CalledProcessError:
                print(f"failed to set executable permission for {script}.")
        else:
            print(f"{script} not found in the current directory.")

def print_final_message():
    print("\nsetup completed successfully.")
    print("all required packages installed.")
    print("scripts made executable.\n")
    print("now you can start the tool by typing:")
    print(">>>>   python ai-terminal-x.py")
    print("   or")
    print(">>>>   ./ai-terminal-x.py\n")
    print("make sure you are in the correct directory when running the command.")

def main():
    print("starting setup for ai-terminal-x...")
    install_system_packages()
    install_python_packages()
    make_scripts_executable()
    print_final_message()

if __name__ == "__main__":
    main()
