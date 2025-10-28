"""
Gmail API setup and send test using Google OAuth directly.
First run will open a browser window to complete OAuth login.
"""

import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from langchain_google_community import GmailToolkit

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://mail.google.com/']

def get_gmail_service():
    """Get Gmail service with OAuth credentials."""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service

def main():
    # Get Gmail service
    service = get_gmail_service()
    
    # Create Gmail toolkit using the authenticated service
    toolkit = GmailToolkit(api_resource=service)

    # Get the tools (includes send/search/read capabilities)
    tools = toolkit.get_tools()
    
    # Print available tools for debugging
    print("Available tools:")
    for tool in tools:
        print(f"- {tool.name}: {tool.description}")

    # Test sending an email directly (optional)
    try:
        create_gmail_draft = next(t for t in tools if t.name == "create_gmail_draft")
    except StopIteration:
        print("gmail_send_message tool not found. Available tools:")
        for tool in tools:
            print(f"  {tool.name}")
        return

    result = create_gmail_draft.run({
        "to": ["jpassynkova@gmail.com"],
        "subject": "Test Email from LangChain Gmail Toolkit",
        "message": "Hello! This is a test message sent via GmailToolkit integration."
    })

    print("Email send result:", result)

if __name__ == "__main__":
    main()
