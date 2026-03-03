import json


class Storage:
    """
    Vastutab LogBooki kirjete salvestamise ja laadimise eest JSON failist.
    """

    @staticmethod
    def save(filename, entries_list):
        """
        Salvestab kirjed JSON faili.
        entries_list on list, kus iga element on dict (LogEntry.to_dict()).
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(entries_list, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Salvestamisel tekkis viga: {e}")

    @staticmethod
    def load(filename):
        """
        Laeb kirjed JSON failist.
        Tagastab listi dict’idega või tühja listi, kui fail puudub/puudulik.
        """
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                else:
                    print("Failis ei ole listi kujul andmeid.")
                    return []
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Faili sisu ei ole korrektne JSON.")
            return []