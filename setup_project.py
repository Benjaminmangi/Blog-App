import os
import subprocess
import sys

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error: {stderr.decode()}")
        sys.exit(1)
    return stdout.decode()

def main():
    # Create Django project
    print("Creating Django project...")
    run_command("django-admin startproject blog_project .")
    
    # Create blog app
    print("Creating blog app...")
    run_command("python manage.py startapp blog")
    
    # Create users app
    print("Creating users app...")
    run_command("python manage.py startapp users")
    
    print("Project setup complete! Please follow the instructions in README.md to continue.")

if __name__ == "__main__":
    main() 