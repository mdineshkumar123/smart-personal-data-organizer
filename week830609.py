def summarize(text):
    sentences = text.split(".")
    return sentences[0] if sentences else text


def summarize_all():
    notes = load_notes()
    for n in notes:
        print("\nOriginal:", n["text"])
        print("Summary:", summarize(n["text"]))