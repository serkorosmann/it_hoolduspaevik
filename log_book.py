import json
from log_entry import LogEntry


class LogBook:
    """
    Logiraamat, mis haldab kõiki IT hoolduskirjeid.
    Vastutab kirje lisamise, kustutamise, otsimise,
    filtreerimise, staatuse muutmise ja
    JSON failist laadimise/salvestamise eest.
    """

    def __init__(self):
        self.entries = []

    # -------------------------
    # Põhifunktsioonid
    # -------------------------

    def add_entry(self, entry: LogEntry):
        """Lisab uue kirje logiraamatusse."""
        self.entries.append(entry)

    def delete_entry(self, created_at: str):
        """Kustutab kirje created_at järgi."""
        self.entries = [
            entry for entry in self.entries
            if entry.created_at != created_at
        ]

    def find_by_keyword(self, keyword: str):
        """Tagastab kirjed, mis sisaldavad märksõna."""
        keyword = keyword.lower()
        return [
            entry for entry in self.entries
            if keyword in entry.title.lower()
            or keyword in entry.description.lower()
        ]

    def filter_by_status(self, status: str):
        """Tagastab kirjed vastavalt staatusele (OPEN/DONE)."""
        return [
            entry for entry in self.entries
            if entry.status == status
        ]

    def change_status(self, created_at: str):
        """
        Muudab kirje staatust OPEN ↔ DONE.
        Tagastab True kui õnnestus, False kui ei leitud.
        """
        for entry in self.entries:
            if entry.created_at == created_at:
                entry.toggle_status()
                return True
        return False

    # -------------------------
    # Failiga töötamine
    # -------------------------

    def save_to_file(self, filename="logbook.json"):
        """Salvestab kõik kirjed JSON faili."""
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                [entry.to_dict() for entry in self.entries],
                file,
                indent=4,
                ensure_ascii=False
            )

    def load_from_file(self, filename="logbook.json"):
        """
        Laeb kirjed JSON failist.
        Kui faili ei ole või see on vigane,
        alustab tühja logiraamatuga.
        Tagastab leitud kirjete arvu.
        """
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

                self.entries = [
                    LogEntry.from_dict(item)
                    for item in data
                ]

                return len(self.entries)

        except FileNotFoundError:
            self.entries = []
            return 0

        except json.JSONDecodeError:
            self.entries = []
            return 0