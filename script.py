import subprocess
import sys

def run_login():
    subprocess.run(['python', 'login.py'])

def run_criminal():
    subprocess.run(['python', 'criminal.py'])

if __name__ == '__main__':
    run_login()
    run_criminal()