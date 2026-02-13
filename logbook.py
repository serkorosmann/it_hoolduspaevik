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