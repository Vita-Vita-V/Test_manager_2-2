import pytest
from main import pridat_ukol, aktualizovat_ukol, odstranit_ukol, zobrazit_ukoly
from database import pripojeni_db

def setup_module(module):
    connection = pripojeni_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM ukoly")  # Vymaže testovací data
    connection.commit()
    cursor.close()
    connection.close()

def test_pridat_ukol_pozitivni():
    pridat_ukol("Testovací úkol", "Popis testu", "probiha")
    connection = pripojeni_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ukoly WHERE nazev='Testovací úkol'")
    vysledek = cursor.fetchone()
    cursor.close()
    connection.close()
    assert vysledek is not None

def test_pridat_ukol_negativni():
    with pytest.raises(Exception):  
        pridat_ukol(None, None, None)

def test_aktualizovat_ukol_pozitivni():
    pridat_ukol("Další úkol", "Další test", "probiha")
    connection = pripojeni_db()
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM ukoly WHERE nazev='Další úkol'")
    ukol_id = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    
    aktualizovat_ukol(ukol_id, "hotovo")
    
    connection = pripojeni_db()
    cursor = connection.cursor()
    cursor.execute("SELECT stav FROM ukoly WHERE id=%s", (ukol_id,))
    stav = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    
    assert stav == "hotovo"

def test_aktualizovat_ukol_negativni():
    with pytest.raises(Exception):  
        aktualizovat_ukol("text místo čísla", "probiha")

def test_odstranit_ukol_pozitivni():
    pridat_ukol("Dočasný úkol", "Test odstranění", "probiha")
    connection = pripojeni_db()
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM ukoly WHERE nazev='Dočasný úkol'")
    ukol_id = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    
    odstranit_ukol(ukol_id)
    
    connection = pripojeni_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ukoly WHERE id=%s", (ukol_id,))
    vysledek = cursor.fetchone()
    cursor.close()
    connection.close()
    
    assert vysledek is None

def test_odstranit_ukol_negativni():
    
    odstranit_ukol(99999)  


