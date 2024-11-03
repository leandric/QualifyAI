from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials
import os

# Ensure the directory exists
output_dir = './curriculos/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the scope of access
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

# Load credentials from the token.json file
creds = Credentials.from_authorized_user_file('token.json', SCOPES)

# Build the Google Drive API service
service = build('drive', 'v3', credentials=creds)

# The ID of the folder you want to list the files from
folder_id = '1ml8bGoNlwyhifYulz33gDlzb7i8R4xs_'

# List files in the folder specified by folder_id
results = service.files().list(
    q=f"'{folder_id}' in parents", fields="files(id, name)"
).execute()

# Retrieve the list of files
files = results.get('files', [])

if not files:
    raise FileNotFoundError('No files found.')
else:
    print('Files:')
    for file in files:
        print(f"{file['name']} ({file['id']})")

        # Download each file from the drive
        request = service.files().get_media(fileId=file['id'])
        file_path = f"./curriculos/{file['name']}"  # Set the path to save the file
        with open(file_path, 'wb') as f:
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f"Download {int(status.progress() * 100)}%.")
