import csv
from modeli import commit

@commit
def pobrisi_tabele(cur):
    """
    Pobriše tabele iz baze.
    """
    cur.execute("DROP TABLE IF EXISTS kategorija;")
    cur.execute("DROP TABLE IF EXISTS kupec;")

@commit
def ustvari_tabele(cur):
    """
    Ustvari tabele v bazi.
    """
    cur.execute("""
        CREATE TABLE kupec (
    id_kupec        INTEGER PRIMARY KEY AUTOINCREMENT,
    davcna_stevilka VARCHAR NOT NULL
                            UNIQUE,
    naslov          VARCHAR NOT NULL,
    ime             VARCHAR NOT NULL
                            UNIQUE,
    kontaktna_oseba VARCHAR

        );
    """)
    cur.execute("""
        CREATE TABLE kategorija (
    id_kategorija INTEGER PRIMARY KEY AUTOINCREMENT
                          NOT NULL
                          UNIQUE,
    ime           VARCHAR NOT NULL
        );
    """)
    