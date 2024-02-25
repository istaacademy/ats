import subprocess
import os
import shutil


# Function to execute shell commands
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error: {stderr.decode('utf-8')}")
        exit(process.returncode)
    return stdout.decode('utf-8')


username = "istaacademy"
password_or_token = "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"

# Define the original and new repository URLs
original_repo_url = "https://github.com/jordan-wright/email.git"
new_repo_url = f"https://{username}:{password_or_token}@github.com/istaacademy/bootcamp-front.git"

# Define the repository name
repo_name = original_repo_url.split('/')[-1].replace('.git', '')

# Clone the existing repository
run_command(['git', 'clone', original_repo_url])

# Create a new folder with the repository name
new_folder_path = os.path.join("/home/esmaeil/Documents/bootcamp-front", repo_name)
os.makedirs(new_folder_path, exist_ok=True)

# Move all files and folders except the .git folder
for item in os.listdir(repo_name):
    s = os.path.join(repo_name, item)
    d = os.path.join(new_folder_path, item)
    if os.path.isdir(s) and '.git' not in s:
        shutil.move(s, d)
    elif os.path.isfile(s):
        shutil.move(s, d)

# Change to the new folder directory
os.chdir("/home/esmaeil/Documents/bootcamp-front")


# Add all files to the new repository
run_command(['git', 'add', '.'])

# Commit the changes
run_command(['git', 'commit', '-m', 'Move files to new folder'])

# Add the new repository URL as a remote
run_command(['git', 'remote', 'set-url', 'origin', new_repo_url])

# Push the changes to the new repository
run_command(['git', 'push', '-u', 'origin', 'main'])

print("Files have been moved and pushed to the new repository.")
