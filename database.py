import mysql.connector

def pripojeni_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # Zde zadejte své heslo k MySQL
            database='ukoly_db'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Chyba při připojení k databázi: {err}")
        return None

def vytvoreni_tabulky():
    connection = pripojeni_db()
    if connection is None:
        return
    
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ukoly (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nazev VARCHAR(255) NOT NULL,
            popis TEXT,
            stav VARCHAR(50) NOT NULL
        );
    ''')
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    vytvoreni_tabulky()
