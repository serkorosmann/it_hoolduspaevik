import json
import os
from models import LogEntry


class LogBook:
    """Klass, mis haldab kõiki logikirjeid ja failimajandust."""

    def __init__(self):
        self.entries = []  # Siia kogume kõik LogEntry objektid

    def add_entry(self, entry):
        """Lisab uue kirje nimekirja."""
        self.entries.append(entry)

    def remove_entry(self, created_at):
        """Kustutab kirje created_at (ID) järgi."""
        original_count = len(self.entries)
        self.entries = [e for e in self.entries if e.created_at != created_at]
        return len(self.entries) < original_count

    def find_entries(self, keyword):
        """Otsib märksõna pealkirjast või kirjeldusest."""
        keyword = keyword.lower()
        return [e for e in self.entries if keyword in e.title.lower() or keyword in e.description.lower()]

    def filter_by_status(self, status):
        """Tagastab kirjed vastavalt staatusele (OPEN/DONE)."""
        return [e for e in self.entries if e.status == status]

    def save_to_json(self, filename="logbook.json"):
        """Salvestab kõik kirjed JSON-faili."""
        data = [e.to_dict() for e in self.entries]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_from_json(self, filename="logbook.json"):
        """Laeb kirjed JSON-failist."""
        if not os.path.exists(filename):
            return "Faili ei ole, alustame tühja raamatuga."

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.entries = []
                for item in data:
                    entry = LogEntry(
                        title=item['title'],
                        description=item['description'],
                        status=item['status'],
                        created_at=item['created_at']
                    )
                    self.entries.append(entry)
            return f" Laetud {len(self.entries)} kirjet."
        except Exception as e:
            return f" Viga faili lugemisel: {e}"

def import_from_json(self, filename):
        """Impordib andmeid failist, valideerib need ja logib vead."""
        if not os.path.exists(filename):
            return f"Faili {filename} ei leitud."

        imported_count = 0
        error_count = 0

        with open(filename, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return "Vigane JSON-faili vorming."

        with open("import_errors.log", "w", encoding="utf-8") as error_file:
            for item in data:
                try:
                    # Üritame luua uut objekti. Kui title või description on
                    # liiga lühikesed, viskab LogEntry ValueError-i.
                    new_entry = LogEntry(
                        title=item.get('title', ''),
                        description=item.get('description', ''),
                        status=item.get('status', 'OPEN'),
                        created_at=item.get('created_at')
                    )
                    self.add_entry(new_entry)
                    imported_count += 1
                except ValueError as e:
                    # Kui tekkis viga, kirjutame selle logifaili
                    error_file.write(f"VIGA: {e} | ANDMED: {item}\n")
                    error_count += 1

        return f"✅ Import lõppenud. Lisati {imported_count} kirjet. Leiti {error_count} viga (vaata import_errors.log)."