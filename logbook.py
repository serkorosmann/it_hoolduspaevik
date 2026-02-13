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
        """Kustutab kirje ID (created_at) järgi."""
        self.entries = [e for e in self.entries if e.created_at != created_at]

    def save_to_json(self, filename="logbook.json"):
        """Salvestab kõik kirjed JSON-faili."""
        data = [e.to_dict() for e in self.entries]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_from_json(self, filename="logbook.json"):
        """Laeb kirjed JSON-failist ja teeb neist LogEntry objektid."""
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
            return f"Laetud {len(self.entries)} kirjet."
        except Exception as e:
            return f"Viga faili lugemisel: {e}"