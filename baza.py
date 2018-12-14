import csv

def pobrisi_tabele(conn):
    """
    Pobriše tabele iz baze.
    """
    conn.execute("DROP TABLE IF EXISTS kategorija;")
    conn.execute("DROP TABLE IF EXISTS kupec;")
    conn.execute("DROP TABLE IF EXISTS status;")
    conn.execute("DROP TABLE IF EXISTS narocilo;")
    conn.execute("DROP TABLE IF EXISTS izdelek;")
    conn.execute("DROP TABLE IF EXISTS narocilo_vsebuje_izdelek;")

def ustvari_tabele(conn):
    """
    Ustvari tabele v bazi.

    """
    conn.execute("""
        CREATE TABLE kupec (
    id_kupec        INTEGER PRIMARY KEY AUTOINCREMENT,
    davcna_stevilka VARCHAR NOT NULL
                            UNIQUE,
    naslov          VARCHAR NOT NULL,
    ime             VARCHAR NOT NULL
                            UNIQUE,
    prezime             VARCHAR NOT NULL
                            UNIQUE,
    kontaktna_oseba VARCHAR

        );
    """)
    conn.execute("""
        CREATE TABLE kategorija (
    id_kategorija INTEGER PRIMARY KEY AUTOINCREMENT
                          NOT NULL
                          UNIQUE,
    ime           VARCHAR NOT NULL
        );
    """)

    conn.execute("""
        CREATE TABLE status (
    id_status INTEGER PRIMARY KEY AUTOINCREMENT
                          NOT NULL
                          UNIQUE,
    naziv_statusa           VARCHAR NOT NULL
        );
    """)

    conn.execute("""
        CREATE TABLE narocilo (
    id_narocilo INTEGER PRIMARY KEY AUTOINCREMENT
                          NOT NULL
                          UNIQUE,
    datum           DATETIME NOT NULL,
    rok_placila           DATETIME NOT NULL,
    kupec_id_kupec REFERENCES kupec(id_kupec),
    status_id_status REFERENCES status(id_status)
        );
    """)

    conn.execute("""
        CREATE TABLE izdelek (
            id_izdelek INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            opis VARCHAR,
            zaloga INTEGER NOT NULL,
            cena DOUBLE NOT NULL,
            kategorija_id_kategorija REFERENCES kategorija(id_kategorija)
        )
    """)

    conn.execute("""
        CREATE TABLE narocilo_vsebuje_izdelek (
            id_narocilo_vsebuje_izdelek INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            kolicina INTEGER NOT NULL,
            popust DOUBLE,
            izdelek_id_izdelek REFERENCES izdelek(id_izdelek),
            narocilo_id_narocilo REFERENCES narocilo(id_narocilo)
        )
    """)

    

def ustvari_bazo(conn):
    """
    Opravi celoten postopek postavitve baze.
    """
    pobrisi_tabele(conn)
    ustvari_tabele(conn)
    # uvozi_filme(conn)
    # uvozi_osebe(conn)
    # uvozi_vloge(conn)
    # uvozi_zanre(conn)


def ustvari_bazo_ce_ne_obstaja(conn):
    """
    Ustvari bazo, če ta še ne obstaja.
    """
    with conn:
        cur = conn.execute("SELECT COUNT(*) FROM sqlite_master")
        if cur.fetchone() == (0, ):
            ustvari_bazo(conn)