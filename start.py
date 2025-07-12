# ---------------------------------------------------------------------------------------------
from dotenv import load_dotenv, find_dotenv
import os
import sys

# Add Shared folder to sys.path
sys.path.append(os.path.abspath("Shared"))

from utils import heading, heading2, heading3, clearConsole, note
from openai import OpenAI

# Load environment variables
load_dotenv(find_dotenv(), override = True)

# Clear console and set working directory
clearConsole()

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print("Current working directory:", os.getcwd())

# Headings
name = os.path.basename(__file__)
heading(f"{name}")
api_key = os.environ.get("api_key")
pinecone_vector_database_key = os.environ.get("pinecone_vector_database_key")
pinecone_environment = os.environ.get("pinecone_environment", "gcp-starter")
# ---------------------------------------------------------------------------------------------
# read settings from .env file

import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

import os
import paramiko

# Connection details
hostname = os.getenv("hostname")
key_path = os.getenv("key_path")
username = os.getenv("username")


# Make sure the key file uses encryption.


print(f"Connecting to {hostname} as {username} using key {key_path}")

current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Current directory: {current_dir}")

# Get full path to the key file
if not key_path.startswith('/'):
    key_path = os.path.join(current_dir, key_path)
if not os.path.exists(key_path):
    print(f"Key file does not exist: {key_path}")
    print("Please check the key path in your .env file.")
    print("Exiting the script.")
    print(f"Using key file: {key_path}")
if not hostname or not username or not key_path:
    print("Please ensure that hostname, username, and key_path are set in your .env file.")
    print("Exiting the script.")    
    print(f"Hostname: {hostname}, Username: {username}, Key Path: {key_path}")    
    exit()


print ("Ready to connect to the EC2 instance...")

# Create SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the EC2 instance using key_filename
ssh.connect(hostname=hostname, username=username, key_filename=key_path)

# Run a command remotely
stdin, stdout, stderr = ssh.exec_command('ls -l ~')

# Print the output
print(stdout.read().decode())

# Close the connection
ssh.close()