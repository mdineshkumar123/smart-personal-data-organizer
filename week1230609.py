# simple placeholder for AI integration

def smart_reply(text):
    return f"AI Suggestion: Improve -> {text}"

def ai_notes():
    notes = load_notes()
    for n in notes:
        print("\nNote:", n["text"])
        print(smart_reply(n["text"]))