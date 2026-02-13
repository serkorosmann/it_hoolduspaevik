import datetime


class LogEntry:
    """Klass, mis kirjeldab ühte IT-hooldustööd."""

    def __init__(self, title, description, status="OPEN", created_at=None):
        # Kui aega pole antud, loome uue ID/aja
        if created_at is None:
            self.created_at = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        else:
            self.created_at = created_at

        # VALIDEERIMINE (Väga oluline punkt juhendis!)
        if len(title) < 4:
            raise ValueError("Pealkiri liiga lühike (min 4 märki)!")
        if len(description) < 10:
            raise ValueError("Kirjeldus liiga lühike (min 10 märki)!")

        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        """Muudab objekti sõnastikuks, et saaksime selle JSON-faili panna."""
        return {
            "created_at": self.created_at,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

    def __str__(self):
        """Kuidas kirjet kasutajale ekraanil kuvatakse."""
        return f"{self.created_at} | [{self.status}] | {self.title} | {self.description}"