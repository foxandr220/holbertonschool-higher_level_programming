#!/usr/bin/python3

def generate_invitiations(template, attendees):
    """Generate invitation files based on a template and list of dictionaries."""
    # -------- 1. Check input types --------
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Invalid input: template should be a string and attendees should be a list of dictionaries.")
        return

    for item in attendees:
        if not isinstance(item, dict):
            print("Invalid input: attendees should be a list of dictionaries.")
            return

    # -------- 2. Handle empty template --------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # -------- 3. Handle empty attendees list --------
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # -------- 4. Process each attendee --------
    index = 1
    for attendee in attendees:
        # Replace missing values with "N/A"
        name = attendee.get("name", "N/A")
        title = attendee.get("event_title", "N/A")
        date = attendee.get("event_date", "N/A")
        location = attendee.get("event_location", "N/A")

        output_text = template.replace("{name}", str(name))
        output_text = output_text.replace("{event_title}", str(title))
        output_text = output_text.replace("{event_date}", str(date))
        output_text = output_text.replace("{event_location}", str(location))

        output_filename = f"output_{index}.txt"

        # -------- 5. Write output file --------
        try:
            with open(output_filename, "w") as f:
                f.write(output_text)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
            return

        index += 1
