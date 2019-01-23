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
    kontaktna_oseba VARCHAR

        );
    """)
    conn.execute("""
        CREATE TABLE kategorija (
    id_kategorija INTEGER PRIMARY KEY AUTOINCREMENT,
    ime           VARCHAR NOT NULL
        );
    """)

    conn.execute("""
        CREATE TABLE status (
    id_status INTEGER PRIMARY KEY AUTOINCREMENT,
    naziv_statusa           VARCHAR NOT NULL
        );
    """)

    conn.execute("""
        CREATE TABLE narocilo (
    id_narocilo INTEGER PRIMARY KEY AUTOINCREMENT,
    datum           DATETIME NOT NULL,
    rok_placila           DATETIME NOT NULL,
    kupec_id_kupec REFERENCES kupec(id_kupec),
    status_id_status REFERENCES status(id_status)
        );
    """)

    conn.execute("""
        CREATE TABLE izdelek (
            id_izdelek INTEGER PRIMARY KEY AUTOINCREMENT,
            opis VARCHAR,
            zaloga INTEGER NOT NULL,
            cena DOUBLE NOT NULL,
            kategorija_id_kategorija INTEGER REFERENCES kategorija(id_kategorija)
        )
    """)

    conn.execute("""
        CREATE TABLE narocilo_vsebuje_izdelek (
            id_narocilo_vsebuje_izdelek INTEGER PRIMARY KEY AUTOINCREMENT,
            kolicina INTEGER NOT NULL,
            popust DOUBLE,
            izdelek_id_izdelek REFERENCES izdelek(id_izdelek),
            narocilo_id_narocilo INTEGER REFERENCES narocilo(id_narocilo)
        )
    """)

def uvozi_kategorije(conn):
    """
    Uvozi podatke o kategorijah ur.
    """
    conn.execute("DELETE FROM kategorija;")
    with open('podatki/kategorije.csv', encoding='UTF-8') as datoteka:
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO kategorija VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_kupce(conn):
    """
    Uvozi podatke o kupcih.
    """
    conn.execute("DELETE FROM kupec;")
    with open('podatki/kupci.csv', encoding='UTF-8') as datoteka: # TODO dodaj encoding
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO kupec VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)


def uvozi_status(conn):
    """
    Uvozi podatke o statusih.
    """
    conn.execute("DELETE FROM status;")
    with open('podatki/status.csv') as datoteka:
        #print("ucitao csv podatke")
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO status VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)


def uvozi_izdelek(conn):
    """
    Uvozi podatke o izdelkih.
    """
    conn.execute("DELETE FROM izdelek;")
    with open('podatki/izdelek.csv') as datoteka:
        #print("ucitao csv podatke")
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO izdelek VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_narocilo(conn):
    """
    Uvozi podatke o naročilih.
    """
    conn.execute("DELETE FROM narocilo;")
    with open('podatki/narocilo.csv') as datoteka:
        #print("ucitao csv podatke")
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO narocilo VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)

def uvozi_narocilo_vsebuje_izdelek(conn):
    """
    Uvozi podatke o naročilih.
    """
    conn.execute("DELETE FROM narocilo_vsebuje_izdelek;")
    with open('podatki/narocilo_vsebuje_izdelek.csv') as datoteka:
        #print("ucitao csv podatke")
        podatki = csv.reader(datoteka)
        stolpci = next(podatki)
        poizvedba = """
            INSERT INTO narocilo_vsebuje_izdelek VALUES ({})
        """.format(', '.join(["?"] * len(stolpci)))
        for vrstica in podatki:
            conn.execute(poizvedba, vrstica)


    #TODO razmisli kako bi sastavio samo jednu (ili manje) funkciju za unos podataka?

def ustvari_bazo(conn):
    """
    Opravi celoten postopek postavitve baze.
    """
    pobrisi_tabele(conn)
    ustvari_tabele(conn)
    # Uvoz podatkov
    uvozi_kategorije(conn)
    uvozi_kupce(conn)
    uvozi_status(conn)
    uvozi_izdelek(conn)
    uvozi_narocilo(conn)
    uvozi_narocilo_vsebuje_izdelek(conn)


def ustvari_bazo_ce_ne_obstaja(conn):
    """
    Ustvari bazo, če ta še ne obstaja.
    """
    with conn:
        cur = conn.execute("SELECT COUNT(*) FROM sqlite_master")
        if cur.fetchone() == (0, ):
            ustvari_bazo(conn)