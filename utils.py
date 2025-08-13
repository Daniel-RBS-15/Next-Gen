import os
import json
import base64
from google.oauth2 import service_account


def get_gcp_credentials():
    """Get GCP credentials, works both locally and on rsconnect"""

    # Priority 1: Direct JSON content from environment variable
    if 'GCP_CREDENTIALS_JSON' in os.environ:
        return service_account.Credentials.from_service_account_info(
            json.loads(os.environ['GCP_CREDENTIALS_JSON'])
        )

    # Priority 2: Base64 encoded JSON from environment variable
    elif 'GCP_CREDENTIALS_BASE64' in os.environ:
        decoded = base64.b64decode(os.environ['GCP_CREDENTIALS_BASE64']).decode('utf-8')
        return service_account.Credentials.from_service_account_info(
            json.loads(decoded)
        )

    # Priority 3: Path to JSON file from environment variable
    elif 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ:
        return service_account.Credentials.from_service_account_file(
            os.environ['GOOGLE_APPLICATION_CREDENTIALS']
        )

    # Priority 4: Local JSON file (for development)
    else:
        try:
            return service_account.Credentials.from_service_account_file(
                'service_account.json'
            )
        except FileNotFoundError:
            raise Exception("No GCP credentials found in environment variables or local file")
