def export_txt():
    notes = load_notes()

    with open("backup.txt", "w") as f:
        for n in notes:
            f.write(f"{n['date']} - {n['text']}\n")

    print("Exported!")