from datetime import datetime


class LogEntry:
    """
    Üks IT-töö või hoolduskirje.
    """

    ALLOWED_STATUSES = ["OPEN", "DONE"]

    def __init__(self, title: str, description: str, status: str = "OPEN", created_at: str = None):
        self.validate_title(title)
        self.validate_description(description)
        self.validate_status(status)

        self.title = title
        self.description = description
        self.status = status

        if created_at:
            self.created_at = created_at
        else:
            self.created_at = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def validate_title(title):
        if not title or len(title.strip()) < 4:
            raise ValueError("Pealkiri peab olema vähemalt 4 tähemärki pikk.")

    @staticmethod
    def validate_description(description):
        if not description or len(description.strip()) < 10:
            raise ValueError("Kirjeldus peab olema vähemalt 10 tähemärki pikk.")

    @classmethod
    def validate_status(cls, status):
        if status not in cls.ALLOWED_STATUSES:
            raise ValueError("Staatus peab olema OPEN või DONE.")

    def toggle_status(self):
        """Vahetab staatuse OPEN ↔ DONE"""
        self.status = "DONE" if self.status == "OPEN" else "OPEN"

    def to_dict(self):
        """Teisendab kirje sõnastikuks JSON jaoks."""
        return {
            "created_at": self.created_at,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Loob LogEntry objekti sõnastikust."""
        return cls(
            title=data["title"],
            description=data["description"],
            status=data["status"],
            created_at=data["created_at"]
        )

    def __str__(self):
        return f"{self.created_at} | [{self.status}] | {self.title} | {self.description}"