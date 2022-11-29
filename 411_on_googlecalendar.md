Collected Knowledge & Wisdom on
# Google Calendar API

## Provides:
This API provides Google Calendar functions, including Events, Calendar, Calendar List, Settings, ACL, and Invitations



### Pain factor: 3
(0=ezpz...5=nightmare)

### Key Provisioning:     
## FOR ALL GOOGLE WORKSPACE APIS:
1. Start up a Google Cloud Project
2. Enable the APIs you want to use in current project -> Getting Started -> Explore and Enable APIs -> Enable APIs and Services
3. Return to the main menu -> "APIs & Services" -> "Credentials"
4. Create your credentials through the "OAuth client ID" option (if you don't have one then you need to configure an OAuth consent screen)
5. Go to "Credentials" -> "Create Credentials" -> "API Key"


### Quotas:
- Maximum 600 Queries per minute per user

---

## The Good:
Users can:
- create an event in their app using events.insert() and include parameters like Location, Event ID, Attendees, event start and end times, and calendarID
- use video and phone conferences in events
- create recurring events
- specify time zone
- decide how to deliver each notification type (event creation, event change, event cancellation, attendee response, agenda)
- use pop-up delivery method supported on mobile platforms and web clients, or use email sent by the server

## The Bad:
- Start and end times must be either both timed or all-day. (Ex: the user can't specify start.date and end.dateTime)
- Need to install Google's Python client library through: "pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib"

## The Ugly:
- Creating a key for the Google Workspace API can be a real hassle because it requires an OAuth client ID
- There are a ton of variables involved in creating events (10+ for the most specific ones)


**Location:** https://developers.google.com/calendar/api

# DISCLAIMER: THIS CARD REQUIRES "pip install" AND OAUTH (do not use right now; too complicated)

---

Accurate as of (last update):    2022-09-26

Contributors:

Jeremy Kwok, pd7  
