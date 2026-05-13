import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# Authenticate
credentials = None

if os.path.exists("token.pkl"):
    with open("token.pkl", "rb") as token:
        credentials = pickle.load(token)

if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secret.json",
            SCOPES
        )
        credentials = flow.run_local_server(port=0)

    with open("token.pkl", "wb") as token:
        pickle.dump(credentials, token)

# Build YouTube service
youtube = build("youtube", "v3", credentials=credentials)

# Upload video
request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "AI Generated Short",
            "description": "Uploaded automatically using Python AI automation.",
            "tags": ["AI", "Shorts", "Automation"],
            "categoryId": "28"
        },
        "status": {
            "privacyStatus": "private"
        }
    },
    media_body=MediaFileUpload("short.MOV")
)  

response = request.execute()

print("Upload Complete!")
print("Video ID:", response["id"])