import json
from log_entry import LogEntry


def import_from_file(logbook, filename):
    """
    Loeb JSON faili, kontrollib kirjed ja lisab LogBooki.
    Vigased kirjed salvestab import_errors.log koos põhjendusega.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Faili '{filename}' ei leitud.")
        return
    except json.JSONDecodeError:
        print(f"Fail '{filename}' on vigane JSON.")
        return

    errors = []

    for item in data:
        try:
            # proovime luua LogEntry
            entry = LogEntry.from_dict(item)
            logbook.add_entry(entry)
        except Exception as e:
            errors.append((item, str(e)))

    # salvesta vigade log
    if errors:
        with open("import_errors.log", "w", encoding="utf-8") as f:
            for item, reason in errors:
                f.write(f"Vigane kirje: {item}\nPõhjus: {reason}\n\n")

    print(f"Import lõppes: {len(logbook.entries)} kirjet lisatud, {len(errors)} vigast kirjet.")