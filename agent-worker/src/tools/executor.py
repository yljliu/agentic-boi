from implementations import calender, email


#Given a tool name and input, find matching implementation and run it
def fetch_tool(tool_name: str, input: dict):
    if tool_name == "create_calender_event":
        return calender.create_calender_event(input)
    elif tool_name == "list_calendar_events":
        return calender.list_calender_events(input)
    else:
        raise ValueError(f"Uknown Tool: {tool_name}")




