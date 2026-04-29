def run_cli():
    while True:
        cmd = input("\n(add/search/exit): ")

        if cmd == "add":
            text = input("Note: ")
            add_note(text)

        elif cmd == "search":
            key = input("Keyword: ")
            results = search_notes(key)
            display(results)

        elif cmd == "exit":
            break