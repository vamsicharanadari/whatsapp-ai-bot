# calendar_handler.py
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


def get_calendar_service():
    # creds.json from Google Cloud Console (OAuth)
    creds = Credentials.from_authorized_user_file("token.json", ["https://www.googleapis.com/auth/calendar"])
    return build("calendar", "v3", credentials=creds)


def create_event(summary, date, time):
    service = get_calendar_service()

    event = {
        "summary": summary,
        "start": {
            "dateTime": f"{date}T{time}:00",
            "timeZone": "America/Chicago"  # Change timezone if needed
        },
        "end": {
            "dateTime": f"{date}T{time}:00",
            "timeZone": "America/Chicago"
        }
    }

    event = service.events().insert(calendarId="primary", body=event).execute()
    return event.get("htmlLink")
