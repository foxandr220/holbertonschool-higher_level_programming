#!/usr/bin/python3

def generate_invitations(template, attendees):
    """Generate invitation files based on a template and list of dictionaries."""
    # ---- Check input types ----
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Invalid input: template should be a string and attendees should be a list of dictionaries.")
        return

    for item in attendees:
        if not isinstance(item, dict):
            print("Invalid input: attendees should be a list of dictionaries.")
            return

    # ---- Empty template ----
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # ---- Empty attendees ----
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ---- Process each attendee ----
    for idx, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A")
        title = attendee.get("event_title", "N/A")
        date = attendee.get("event_date", "N/A")
        loc = attendee.get("event_location", "N/A")

        result = template.replace("{name}", str(name))
        result = result.replace("{event_title}", str(title))
        result = result.replace("{event_date}", str(date))
        result = result.replace("{event_location}", str(loc))

        filename = f"output_{idx}.txt"
        with open(filename, "w") as f:
            f.write(result)
