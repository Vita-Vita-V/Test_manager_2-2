from database import pripojeni_db

def pridat_ukol(nazev, popis, stav):
    connection = pripojeni_db()
    if connection is None:
        return
    
    cursor = connection.cursor()
    sql = "INSERT INTO ukoly (nazev, popis, stav) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nazev, popis, stav))
    connection.commit()
    cursor.close()
    connection.close()

def zobrazit_ukoly():
    connection = pripojeni_db()
    if connection is None:
        return
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ukoly")
    for (id, nazev, popis, stav) in cursor:
        print(f"{id}: {nazev} - {popis} [{stav}]")
    cursor.close()
    connection.close()

def aktualizovat_ukol(ukol_id, novy_stav):
    connection = pripojeni_db()
    if connection is None:
        return
    
    cursor = connection.cursor()
    sql = "UPDATE ukoly SET stav = %s WHERE id = %s"
    cursor.execute(sql, (novy_stav, ukol_id))
    connection.commit()
    cursor.close()
    connection.close()

def odstranit_ukol(ukol_id):
    connection = pripojeni_db()
    if connection is None:
        return
    
    cursor = connection.cursor()
    sql = "DELETE FROM ukoly WHERE id = %s"
    cursor.execute(sql, (ukol_id,))
    connection.commit()
    cursor.close()
    connection.close()

def hlavni_menu():
    while True:
        print("\n1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Aktualizovat úkol")
        print("4. Odstranit úkol")
        print("5. Konec")
        volba = input("Vyberte možnost: ")
        
        if volba == '1':
            nazev = input("Název úkolu: ")
            popis = input("Popis: ")
            stav = input("Stav: ")
            pridat_ukol(nazev, popis, stav)
        elif volba == '2':
            zobrazit_ukoly()
        elif volba == '3':
            ukol_id = int(input("ID úkolu: "))
            novy_stav = input("Nový stav: ")
            aktualizovat_ukol(ukol_id, novy_stav)
        elif volba == '4':
            ukol_id = int(input("ID úkolu: "))
            odstranit_ukol(ukol_id)
        elif volba == '5':
            break
        else:
            print("Neplatná volba. Zkuste to znovu.")

if __name__ == "__main__":
    hlavni_menu()
