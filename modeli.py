import baza
import sqlite3

conn = sqlite3.connect('trgovina5.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute('PRAGMA foreign_keys = ON')
conn.execute("PRAGMA encoding = 'UTF-8'")

def poisci_kupca(niz):
    """
    Funkcija, ki vrne šifre vseh filmov, katerih naslov vsebuje dani niz.

    >>> poisci_filme('potter')
    [241527, 295297, 304141, 330373, 373889, 417741, 926084, 1201607]
    """
    poizvedba = """
        SELECT id_kupec
        FROM kupec
        WHERE ime LIKE ?
        ORDER BY ime
    """
    return [id_kupca for (id_kupca,) in conn.execute(poizvedba, ['%' + niz + '%'])]

def podatki_kupcev(idji_kupcev):
    """
    Vrne osnovne podatke vseh kupceu z danimi IDji.

    >>> podatki_filmov([79470, 71853])
    [(71853, 'Monty Python and the Holy Grail', 1975), (79470, 'Life of Brian', 1979)]
    """
    poizvedba = """
        SELECT id_kupec, ime, naslov
        FROM kupec
        WHERE id_kupec IN ({})
        ORDER BY ime
    """.format(', '.join(len(idji_kupcev) * ['?']))
    return conn.execute(poizvedba, idji_kupcev).fetchall()

def podatki_kupca(id_kupca):
    """
    Vrne podatke o filmu z danim IDjem.

    >>> podatki_filma(71853)
    ('Monty Python and the Holy Grail', 1975, 91, 8.3, ['Comedy', 'Fantasy', 'Adventure'],
     [(92, 'igralec'), (416, 'igralec'), (416, 'reziser'), (1037, 'igralec'), (1385, 'igralec'), (1402, 'reziser')])
    """
    poizvedba = """
        SELECT ime, naslov, davcna_stevilka, kontaktna_oseba
        FROM kupec
        WHERE id_kupec = ?
    """
    cur = conn.cursor()
    cur.execute(poizvedba, [id_kupca])
    osnovni_podatki = cur.fetchone()
    if osnovni_podatki is None:
        return None
    else:
        ime, naslov, davcna_stevilka, kontaktna_oseba = osnovni_podatki
       
        return ime, naslov, davcna_stevilka, kontaktna_oseba


# 2) Izdelek
def podatki_izdelkov(idji_izdelkov):
    """
    Vrne osnovne podatke vseh izdelkih z danimi IDji.

    >>> podatki_filmov([79470, 71853])
    [(71853, 'Monty Python and the Holy Grail', 1975), (79470, 'Life of Brian', 1979)]
    """
    poizvedba = """
        SELECT id_izdelek, opis, cena
        FROM izdelek
        WHERE id_izdelek IN ({})
        ORDER BY opis
    """.format(', '.join(len(idji_izdelkov) * ['?']))
    return conn.execute(poizvedba, idji_izdelkov).fetchall()
    


def poisci_izdelek(niz):
    
    """
    Funkcija, ki vrne šifre vseh filmov, katerih naslov vsebuje dani niz.

    >>> poisci_filme('potter')
    [241527, 295297, 304141, 330373, 373889, 417741, 926084, 1201607]
    """
    poizvedba = """
        SELECT id_izdelek
        FROM izdelek
        WHERE opis LIKE ?
        ORDER BY opis
    """
    return [id_izdelek for (id_izdelek,) in conn.execute(poizvedba, ['%' + niz + '%'])]


def podatki_izdelka(id_izdelka):
    """
    Vrne podatke o konkretnom izdelku z danim IDjem.

    >>> podatki_filma(71853)
    ('Monty Python and the Holy Grail', 1975, 91, 8.3, ['Comedy', 'Fantasy', 'Adventure'],
     [(92, 'igralec'), (416, 'igralec'), (416, 'reziser'), (1037, 'igralec'), (1385, 'igralec'), (1402, 'reziser')])
    """
    poizvedba = """
        SELECT opis, zaloga, cena, kategorija_id_kategorija
        FROM izdelek
        WHERE id_izdelek = ?
    """
    cur = conn.cursor()
    cur.execute(poizvedba, [id_izdelka])
    osnovni_podatki = cur.fetchone()
    if osnovni_podatki is None:
        return None
    else:
        opis, zaloga, cena, kategorija_id_kategorija = osnovni_podatki
        poizvedba_za_kategorije = """
            SELECT kategorija.ime
            FROM kategorija
            WHERE kategorija.id_kategorija = ?
        """
        cur.execute(poizvedba_za_kategorije, kategorija_id_kategorija)
        kategorija = cur.fetchone()
       
        return opis, zaloga, cena, kategorija


def podatki_narocil(idji_narocil):
    """
    Vrne osnovne podatke vseh izdelkih z danimi IDji.

    >>> podatki_filmov([79470, 71853])
    [(71853, 'Monty Python and the Holy Grail', 1975), (79470, 'Life of Brian', 1979)]
    """
    poizvedba = """
        SELECT id_narocilo, kupec.ime
        FROM narocilo
        WHERE id_narocilo IN ({})
    """.format(', '.join(len(idji_narocil) * ['?']))
    return conn.execute(poizvedba, idji_narocil).fetchall()


def poisci_narocila(niz):
    """
    Funkcija, ki vrne šifre vseh filmov, katerih naslov vsebuje dani niz.

    >>> poisci_filme('potter')
    [241527, 295297, 304141, 330373, 373889, 417741, 926084, 1201607]
    """
    poizvedba = """
        SELECT id_narocilo
        FROM narocilo
        WHERE datum = ?
    """
    return [id_narocila for (id_narocila,) in conn.execute(poizvedba, ['%' + niz + '%'])]


def podatki_narocila(id_narocila):
    """
    Vrne podatke o konkretnom izdelku z danim IDjem.

    >>> podatki_filma(71853)
    ('Monty Python and the Holy Grail', 1975, 91, 8.3, ['Comedy', 'Fantasy', 'Adventure'],
     [(92, 'igralec'), (416, 'igralec'), (416, 'reziser'), (1037, 'igralec'), (1385, 'igralec'), (1402, 'reziser')])
    """
    poizvedba = """
        SELECT id_narocilo, datum, rok_placila, kupec.ime, status.naziv_statusa
        FROM narocilo
            JOIN kupec ON kupec_id_kupec = kupec.id_kupec
            JOIN status ON status_id_status = status.id_status
        WHERE id_narocilo = ?
    """
    cur = conn.cursor()
    cur.execute(poizvedba, [id_narocila])
    osnovni_podatki = cur.fetchone() #konkretno naročilo
    if osnovni_podatki is None:
        return None
    else:
        id_narocilo, datum, rok_placila, kupec, status = osnovni_podatki
        poizvedba_za_izdelke = """
            SELECT izdelek.opis, izdelek.cena, kolicina, popust
            FROM narocilo_vsebuje_izdelek
                JOIN izdelek ON izdelek_id_izdelek = izdelek.id_izdelek
            WHERE narocilo_id_narocilo = ?
        """
        cur.execute(poizvedba_za_izdelke, id_narocila)
        izdelki = cur.fetchall()
       
        return id_narocilo, datum, rok_placila, kupec, status, izdelki

# def commit(fun):
#     """
#     Dekorator, ki ustvari kurzor, ga poda dekorirani funkciji,
#     in nato zapiše spremembe v bazo.
#     Originalna funkcija je na voljo pod atributom nocommit.
#     """
#     def funkcija(*largs, **kwargs):
#         cur = conn.cursor()
#         ret = fun(cur, *largs, **kwargs)
#         conn.commit()
#         cur.close()
#         return ret
#     funkcija.__doc__ = fun.__doc__
#     funkcija.__name__ = fun.__name__
#     funkcija.__qualname__ = fun.__qualname__
#     fun.__qualname__ += '.nocommit'
#     funkcija.nocommit = fun
#     return funkcija