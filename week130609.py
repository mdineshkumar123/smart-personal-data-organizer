import json
from datetime import datetime

DB_FILE = "notes.json"

def load_notes():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_notes(notes):
    with open(DB_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(text, tags=None):
    if tags is None:
        tags = []

    notes = load_notes()
    note = {
        "text": text,
        "tags": tags,
        "date": str(datetime.now())
    }
    notes.append(note)
    save_notes(notes)

if __name__ == "__main__":
    add_note("Start smart organizer", ["project"])