def ranked_search(keyword):
    notes = load_notes()
    keyword = keyword.lower()

    results = []

    for note in notes:
        text = note["text"].lower()
        tags = note["tags"]

        score = 0

        if keyword in text:
            score += 2

        for t in tags:
            if keyword in t.lower():
                score += 3

        if score > 0:
            results.append((score, note))

    return sorted(results, reverse=True)