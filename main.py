from models import LogEntry
from logbook import LogBook

def show_menu():
    print("\n--- IT-HOOLDUSPÄEVIK ---")
    print("1. Lisa uus logikirje")
    print("2. Kuva kõik kirjed")
    print("3. Otsi märksõna järgi")
    print("4. Filtreeri staatuse järgi (OPEN/DONE)")
    print("5. Muuda kirje staatust")
    print("6. Kustuta kirje (aja järgi)")
    print("7. Salvesta ja välju")
    return input("Vali tegevus (1-7): ")

def main():
    book = LogBook()
    print(book.load_from_json())

    while True:
        choice = show_menu()

        if choice == "1":
            title = input("Sisesta pealkiri (min 4 märki): ")
            desc = input("Sisesta kirjeldus (min 10 märki): ")
            try:
                new_entry = LogEntry(title, desc)
                book.add_entry(new_entry)
                print("Kirje lisatud!")
            except ValueError as e:
                print(f"VIGA: {e}")

        elif choice == "2":
            if not book.entries:
                print("Logiraamat on tühi.")
            else:
                for entry in book.entries:
                    print(entry)

        elif choice == "3":
            keyword = input("Sisesta märksõna: ")
            results = book.find_entries(keyword)
            if results:
                for r in results:
                    print(r)
            else:
                print("Märksõnaga kirjeid ei leitud.")

        elif choice == "4":
            stat = input("Vali staatus (OPEN/DONE): ").upper()
            results = book.filter_by_status(stat)
            for r in results:
                print(r)

        elif choice == "5":
            time_id = input("Sisesta kirje kellaaeg (ID), mida muuta: ")
            for e in book.entries:
                if e.created_at == time_id:
                    e.status = "DONE" if e.status == "OPEN" else "OPEN"
                    print(f"Staatus muudetud: {e.status}")
                    break
            else:
                print("Sellise ajaga kirjet ei leitud.")

        elif choice == "6":
            time_id = input("Sisesta kustutatava kirje kellaaeg (ID): ")
            if book.remove_entry(time_id):
                print("Kirje kustutatud!")
            else:
                print("Kirjet ei leitud.")

        elif choice == "7":
            book.save_to_json()
            print("Andmed salvestatud. Head aega!")
            break

        else:
            print("Tundmatu valik, proovi uuesti.")

if __name__ == "__main__":
    main()