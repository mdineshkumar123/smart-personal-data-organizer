def search_notes(keyword):
    notes = load_notes()
    keyword = keyword.lower()

    results = []

    for note in notes:
        text = note.get("text", "").lower()
        tags = " ".join(note.get("tags", [])).lower()

        if keyword in text or keyword in tags:
            results.append(note)

    return results


def display(results):
    for i, n in enumerate(results, 1):
        print(f"\n{i}. {n['text']}")
        print("Tags:", ", ".join(n["tags"]))
        print("Date:", n["date"])