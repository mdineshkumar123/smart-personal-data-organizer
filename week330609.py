def auto_tag(text):
    rules = {
        "python": "coding",
        "meeting": "work",
        "gym": "health"
    }

    tags = []
    for key, value in rules.items():
        if key in text.lower():
            tags.append(value)

    return tags


def add_note_auto(text):
    tags = auto_tag(text)
    add_note(text, tags)