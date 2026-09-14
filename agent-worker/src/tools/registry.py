import json
import anthropic

"""
List of Tools of our Personal Assistant

1. CALENDER
2. WEB SEARCH
3. READ/WRITE EMAIL

"""

tools = [
    {
        "name": "create_calender_event",
        "description": "Create event on Google calender",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string",  "format": "date-time"},
                "guests": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                    },
                "location": {"type": "string"},
                "timeZone": {"type": "string"},
                "recurrence": {
                    "type": "string",
                    "description": "If a reccurence is given, format it such as RRULE:FREQ=DAILY"
                },
                "count": {"type": "integer"},
            },
            "required": ["title", "start", "end", "timeZone"]
        }
    },
    {
        "name": "list_calender_events",
        "description": "List events for the day on Google Calender",
        "input_schema": {
            "type": "object",
            "properties": {
                "start": {"type": "string",  "format": "date-time"},
                "end": {"type": "string",  "format": "date-time"},
                "location_type": {
                    "type": "string",
                    "enum": ["physical", "virtual"],
                    "description": "Filter events by whether they occur in person or online. Omit this field entirely to include all events regardless of location.",
                },
                "maxResults": {"type": "integer", "default": 10}
            },
            "required": ["start", "end"]
        }
    },
    {
        "name": "read_emails",
        "description": "Fetch the latest emails",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "default": "in:inbox",
                },
                "max_results": {
                    "type": "integer",
                    "default": 10,
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "write_emails",
        "description": "Write and send emails",
        "input_schema": {
            "type": "object", 
            "properties": {
                "to": {"type": "string", "format": "email"},
                "body": {
                    "type": "string",
                    "description": "Draft an email given the topic of what the user has written"
                },
                "subject": {
                    "type": "string",
                    "description": "The header will be the topic of the body summed up in less than 10 words"
                } 
            },
            "required": ["to", "body", "subject"]
        }
    },
        {
        "type": "web_search_20250305",
        "name": "web_search"
    },
]







