import os.path
import io
import webbrowser
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from src.utils_dycrypt import decrypt_string
from dotenv import load_dotenv
load_dotenv()

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive"]


key = os.getenv("encryptkey")
client_id=decrypt_string(os.getenv("client_id"),key)
client_secret=decrypt_string(os.getenv("client_secret"),key)
project_id=os.getenv("project_id")
redirecturi=os.getenv("redirect_uri")


def getfilefromdrive(fileId, fileName):
  try:
    print(fileName)
    with open(f'translations/{fileName}.json', 'r', encoding='utf-8')as readfile:
      file = readfile.read()
      print(file)
      return file
  except Exception as e:
    return None

  """Shows basic usage of the Drive v3 API.
  Prints the names and ids of the first 10 files the user has access to.
  """
  """  creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
      creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        config={
                    "installed": {
                        "client_id": client_id,
                        "project_id": project_id,
                        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                        "token_uri": "https://oauth2.googleapis.com/token",
                        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                        "client_secret": client_secret,
                        "redirect_uris": [
                            redirecturi
                        ]
                    }
                }
        flow =InstalledAppFlow.from_client_config(config,SCOPES)
        #flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
        flow.run_local_server()
        creds = flow.run_local_server(host=redirecturi,port=8080)
      # Save the credentials for the next run
      with open("token.json", "w") as token:
        token.write(creds.to_json()) """

  """ try:
    
    service_account_json_key = '/Users/muhammadsuleman/Downloads/khan-427613-a18c98aab7d5.json'
    creds = service_account.Credentials.from_service_account_file(
                              filename=service_account_json_key, 
                              scopes=SCOPES)
    service = build("drive", "v3", credentials=creds)
    # Step 3: Specify the file ID
    file_id = fileId  # Replace with your file ID

    # Step 4: Read the file content
    request = service.files().get_media(fileId=file_id)
    file_content = io.BytesIO()
    downloader = MediaIoBaseDownload(file_content, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()

    file_content.seek(0)
    content = file_content.read().decode('utf-8')  # Assuming the file is a text file

    print(content)
    return content

  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")
    return None """


#if __name__ == "__main__":
#  main()