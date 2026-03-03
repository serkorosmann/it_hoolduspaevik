# IT Hoolduspäevik

**Autor:** Serko Rosmann  

## Projekti kirjeldus
IT hoolduspäevik on Pythonis loodud rakendus, mis võimaldab hallata IT-töid ja hooldusi, näiteks:

- arvuti parandamine  
- tarkvara paigaldus  
- võrgu probleemide lahendamine  

Rakendus koosneb kahest osast:

1. **CLI (konsoolirakendus)**
2. **GUI (Tkinter, boonus)**

Kõik andmed salvestatakse JSON faili (`logbook.json`) ja vajadusel imporditakse vigaseid kirjeid (`importer.py`).

---

## Failistruktuur

- `log_entry.py` – LogEntry klass (üks kirje)  
- `log_book.py` – LogBook klass (kogu logiraamat)  
- `main.py` – CLI kasutajaliides  
- `importer.py` – vigaste failide import  
- `storage.py` – JSON andmete laadimine ja salvestamine  
- `gui.py` – Tkinter GUI (boonus)  
- `.gitignore` – tühjade logi- ja andmefailide ignoreerimine  
- `README.md` – projekti dokumentatsioon  

---

## CLI kasutus

1. Käivita terminalis:

```bash
python main.py
````
2. Kuvatakse menüü

```bash
=== IT HOOLDUSPÄEVIK ===
1. Lisa uus kirje
2. Kuvada kõik kirjed
3. Otsi märksõna järgi
4. Filtreeri staatuse järgi
5. Muuda kirje staatust
6. Kustuta kirje
7. Salvesta ja välju
```
3. Menüüvalikud - samm-sammult:
```bash
1. Lisa uus kirje: Sisesta pealkiri (vähemalt 4 tähemärki) ja kirjeldus (vähemalt 10 tähemärki). Kui sisend on liiga lühike, kuvatakse viga.
2. Kuvada kõik kirjed: Kõik kirjed kuvatakse formaadis: DD.MM.YYYY HH:MM:SS | [STAATUS] | Pealkiri | Kirjeldus
3. Otsi märksõna järgi: Sisesta märksõna, otsitakse nii pealkirjast kui kirjeldusest ja kuvatakse sobivad kirjed.
4. Filtreeri staatuse järgi: Sisesta "OPEN" või "DONE", kuvatakse ainult sobiva staatusega kirjed.
5. Muuda kirje staatust: Sisesta kirje `created_at` kuupäev ja kellaaeg (näiteks ´06.02.2026 14:03:12`). Staatust muudetakse OPEN <> DONE.
6. Kustuta kirje: Sisesta kirje `created_at`. Kirje kustutatakse, kui see eksisteerib.
7. Salvesta ja välju: Kõik kirjed salvestatakse `logbook.json`faili ja progamm sulgub.
````
## GUI kasutus
1. Käivita GUI: python gui.py
2. Avaaken kuvab tabeli kõigi kirjetega. Iga kirje näitab: aeg (`created_at`)
3. Nupud ja funktsioonid
```bash
Lisa - avab dialoogi, kus sisestad pealkirja ja kirjelduse.
Kustuta - valitud kirje kustutatakse tabelist ja LogBookist.
Muuda staatus - valitud kirje staatust muudetakse OPEN <> DONE.
Salvesta - kõik kirjed salvestatakse JSON faili (logbook.json).
```
4. Veateated
```bash
Kui pealkiri või kirjeldus on tühi, kuvatakse hoiatus.
Kui JSON fail on vigane või puudub, GUI alustab tühja LogBookiga.
```
## Importer
Loeb JSON faili ja kontrollib iga kirjet.
Korrektsed lisatakse LogBooki.
Vigased salvestatakse `import_errors.log` koos põhjendusega.

Näide:
```bash
```python
from log_book import LogBook
from importer import import_from_file

logbook = LogBook()
import_from_file(logbook, "sample_import.json")
````

## Storage
Vastutab LogBooki andmete laadimise ja salvstamise eest JSON failist.

Näide:
```bash
from storage import Storage
from log_entry import LogEntry

# Salvestamine
Storage.save("logbook.json", [entry.to_dict() for entry in logbook.entries])

# Laadimine
data = Storage.load("logbook.json")
logbook.entries = [LogEntry.from_dict(item) for item in data]
```