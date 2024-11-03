import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Define the scope of access required
# These scopes allow reading and modifying files on Google Drive
SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/drive.metadata.readonly"
]

# Initialize the credentials variable
creds = None

# Check if the token.json file exists in the current directory
# This file stores the access credentials
if os.path.exists('token.json'):
    # If it exists, load the credentials from the token.json file
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    print('Credentials loaded from token.json.')

# Check if credentials do not exist or are invalid/expired
if not creds or not creds.valid:
    # If the credentials exist but are expired and can be refreshed
    if creds and creds.expired and creds.refresh_token:
        # Refresh the credentials using the refresh token
        creds.refresh(Request())
        print('Credentials successfully refreshed.')
    else:
        # If no valid credentials are available, start the OAuth authorization flow
        print('Starting the OAuth authorization flow...')
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)  # Run local server for authorization
        print('Authorization completed.')

    # Save the new or refreshed credentials to the token.json file
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
        print('Credentials saved to token.json.')
