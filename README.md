Projekt: Správce úkolů s MySQL

Tento projekt je jednoduchý správce úkolů, který ukládá jednotlivé úkoly do MySQL databáze. Obsahuje funkce pro přidání, aktualizaci a odstranění úkolů a je doplněn o testy pomocí pytest.

Struktura souborů

projekt_ukoly/
│-- main.py          # Hlavní soubor pro práci s úkoly
│-- database.py      # Připojení k MySQL a inicializace tabulky
│-- test_ukoly.py    # Testy pro funkce
│-- requirements.txt # Seznam potřebných knihoven
│-- README.md        # Dokumentace k projektu

1. Instalace a spuštění projektu

1.1. Instalace závislostí

Nejprve nainstalujte všechny potřebné balíčky:

pip install -r requirements.txt

1.2. Vytvoření MySQL databáze

Připojte se k MySQL a vytvořte databázi:

CREATE DATABASE ukoly_db;
USE ukoly_db;

Poté spusťte database.py, který vytvoří potřebnou tabulku:

python database.py

1.3. Spuštění hlavního programu

Program spusťte příkazem:

python main.py

2. Popis souborů

database.py

Připojuje se k MySQL databázi

Vytváří tabulku ukoly, pokud ještě neexistuje

main.py

Obsahuje následující funkce:

pridat_ukol(nazev, popis, stav) – Přidání úkolu do databáze

aktualizovat_ukol(ukol_id, novy_stav) – Aktualizace stavu úkolu

odstranit_ukol(ukol_id) – Odstranění úkolu podle ID

test_ukoly.py

Obsahuje testovací funkce pomocí pytest. Každá funkce má pozitivní a negativní test:

test_pridat_ukol_pozitivni() – Ověří správné přidání úkolu

test_pridat_ukol_negativni() – Ověří reakci na neplatné vstupy

test_aktualizovat_ukol_pozitivni() – Ověří aktualizaci úkolu

test_aktualizovat_ukol_negativni() – Testuje neplatný stav

test_odstranit_ukol_pozitivni() – Ověří správné odstranění úkolu

test_odstranit_ukol_negativni() – Testuje odstranění neexistujícího úkolu

requirements.txt

Seznam potřebných knihoven:

mysql-connector-python
pytest

3. Jak spustit testy

Pro spuštění testů zadejte příkaz:

pytest -v test_ukoly.py

4. Poznámky

Testovací data jsou po každém testu automaticky smazána.

Program obsahuje smysluplné chybové hlášky.
