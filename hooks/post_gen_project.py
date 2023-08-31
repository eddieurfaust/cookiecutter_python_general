import os
import platform
import subprocess
import configparser
import requests

def create_virtualenv():
    print("Creating virtual environment...")
    if platform.system() == "Windows":
        subprocess.run(["python", "-m", "venv", ".venv"])
    else:
        subprocess.run(["python3", "-m", "venv", ".venv"])

def install_dependencies():
    print("Installing dependencies...")
    if platform.system() == "Windows":
        subprocess.run([".venv\\Scripts\\pip", "install", "pylint", "black"])
    else:
        subprocess.run([".venv/bin/pip", "install", "pylint", "black"])

def download_pylintrc():
    print("Downloading .pylintrc from Google Style Guide...")
    url = 'https://raw.githubusercontent.com/google/styleguide/gh-pages/pylintrc'
    try:
        r = requests.get(url)
        r.raise_for_status()
        with open('.pylintrc', 'wb') as f:
            f.write(r.content)
    except requests.RequestException as e:
        print(f"Failed to download .pylintrc: {e}")
        exit(1)

def update_pylintrc(file_path):
    print("Updating .pylintrc...")
    config = configparser.ConfigParser()
    config.read(file_path)

    if 'FORMAT' not in config:
        config.add_section('FORMAT')

    config['FORMAT']['indent-string'] = "'    '"
    config['FORMAT']['max-line-length'] = '120'

    with open(file_path, 'w') as configfile:
        config.write(configfile)

def initialize_git():
    print("Initializing Git repository...")
    subprocess.run(["git", "init", "."])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initial commit"])

if __name__ == "__main__":
    create_virtualenv()
    install_dependencies()
    download_pylintrc()
    update_pylintrc('./.pylintrc')
    initialize_git()
    print("Project setup complete.")
