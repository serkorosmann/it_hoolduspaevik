from log_book import LogBook
from log_entry import LogEntry


def print_menu():
    print("\n=== IT HOOLDUSPÄEVIK ===")
    print("1. Lisa uus kirje")
    print("2. Kuvada kõik kirjed")
    print("3. Otsi märksõna järgi")
    print("4. Filtreeri staatuse järgi")
    print("5. Muuda kirje staatust")
    print("6. Kustuta kirje")
    print("7. Salvesta ja välju")


def main():
    logbook = LogBook()
    count = logbook.load_from_file()

    if count:
        print(f"Leiti {count} kirjet.")
    else:
        print("Kirjeid ei leitud. Alustame tühja logiraamatuga.")

    while True:
        print_menu()
        choice = input("Vali tegevus: ")

        if choice == "1":
            # Lisa uus kirje
            try:
                title = input("Sisesta töö pealkiri: ")
                description = input("Sisesta töö kirjeldus: ")
                entry = LogEntry(title, description)
                logbook.add_entry(entry)
                print("Kirje lisatud!")
            except ValueError as e:
                print("Viga:", e)

        elif choice == "2":
            # Kuvada kõik kirjed
            if not logbook.entries:
                print("Kirjeid ei ole.")
            for entry in logbook.entries:
                print(entry)

        elif choice == "3":
            # Otsi märksõna järgi
            keyword = input("Sisesta märksõna: ")
            results = logbook.find_by_keyword(keyword)
            if results:
                for entry in results:
                    print(entry)
            else:
                print("Ühtegi kirjet ei leitud.")

        elif choice == "4":
            # Filtreeri staatuse järgi
            status = input("Sisesta staatus (OPEN/DONE): ").upper()
            if status not in ["OPEN", "DONE"]:
                print("Lubatud on ainult OPEN või DONE")
                continue
            results = logbook.filter_by_status(status)
            if results:
                for entry in results:
                    print(entry)
            else:
                print("Ühtegi kirjet ei leitud.")

        elif choice == "5":
            # Muuda staatust
            created_at = input("Sisesta kirje created_at: ")
            if logbook.change_status(created_at):
                print("Staatus muudetud!")
            else:
                print("Kirjet ei leitud.")

        elif choice == "6":
            # Kustuta kirje
            created_at = input("Sisesta kustutatava kirje created_at: ")
            logbook.delete_entry(created_at)
            print("Kirje kustutatud (kui eksisteeris).")

        elif choice == "7":
            # Salvesta ja välju
            logbook.save_to_file()
            print("Andmed salvestatud. Head aega!")
            break

        else:
            print("Vale valik.")


if __name__ == "__main__":
    main()