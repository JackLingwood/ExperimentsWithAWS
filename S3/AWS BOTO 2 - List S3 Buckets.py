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


local_s3_save_path = os.getenv("local_s3_save_path","")
bucket_name = os.getenv("bucket_name", "")
bucket_subfolder_name = os.getenv("bucket_subfolder_name", "")
bucket_select_text = os.getenv("bucket_select_text", "")    

if not bucket_name or not bucket_subfolder_name or not bucket_select_text or not local_s3_save_path:
    print("Please set the bucket_name, bucket_subfolder_name, bucket_select_text, and local_s3_save_path in your .env file.")
    print("Exiting the script.")
    quit()




import boto3

# Use the default profile or another existing one
session = boto3.Session(profile_name="production")  # Replace "default" if needed
s3 = session.client("s3")

response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]

print("S3 Buckets:")
for bucket in buckets:
    print(bucket)




print(f"Using bucket: {bucket_name} with subfolder: {bucket_subfolder_name}")       

response = s3.list_objects_v2(Bucket=bucket_name, Prefix=bucket_subfolder_name)

inner_count = 0
max_downloads = 10000

import os
#output_folder = r"C:\Code\AI\Certifications"

paginator = s3.get_paginator('list_objects_v2')
for page in paginator.paginate(Bucket=bucket_name, Prefix=bucket_subfolder_name):
    for obj in page.get('Contents', []):
        #print(obj['Key'])


        txt = obj['Key']
        if bucket_select_text in txt and txt.endswith(".jpg"):
            inner_count += 1
            print(f"{txt}")
            # Prepare local path (flatten: all files in output_folder)
            filename = os.path.basename(txt)
            local_path = os.path.join(local_s3_save_path, filename)
            print(f"Local path: {local_path}")
            # Download the file
            #s3.download_file(bucket_name, txt, local_path)
            print(f"Downloaded {txt} to {local_path}")
        if (inner_count > max_downloads):
            print(f"Stopping after {max_downloads} objects.")
            break
    if inner_count > max_downloads:
        break



