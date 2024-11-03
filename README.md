# QualifyAI

**QualifyAI** is a project that downloads resumes from Google Drive and analyzes them using AI to select the best resumes for a specific job position.

## Environment Setup

### 1. Enable the Google Drive API

1. Go to the [Google Cloud API Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Navigate to **Library** and enable the **Google Drive API**.
4. Go to **Credentials** and create credentials of type **OAuth 2.0**.
5. Download the `credentials.json` file and place it in the root of the project.

### 2. Install Dependencies

The project uses [Poetry](https://python-poetry.org/) to manage dependencies. To install the dependencies, follow the steps below:

```bash
# Install Poetry if it's not already installed
pip install poetry

# Install the project's dependencies
poetry install
```

### 3. Authenticate Access to the Google Drive API

Run the `authenticate.py` script to start the authentication process and generate the `token.json` file, which will store the access credentials.

```bash
# Run the authentication script
poetry run python authenticate.py
```

This script does the following:
- Checks if the `token.json` file exists.
- If `token.json` does not exist or if the credentials are expired, it starts the OAuth 2.0 authorization flow for authentication.
- Saves the new or refreshed credentials to `token.json` in the project root.

## Under Development...