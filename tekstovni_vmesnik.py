import modeli

def izberi_moznost(moznosti):
    """
    Funkcija, ki izpiše seznam možnosti in vrne indeks izbrane možnosti.

    Če na voljo ni nobene možnosti, izpiše opozorilo in vrne None.
    Če je na voljo samo ena možnost, vrne 0.

    >>> izberi_moznost(['jabolko', 'hruška', 'stol'])
    1) jabolko
    2) hruška
    3) stol
    Vnesite izbiro > 2
    1
    >>> izberi_moznost([])
    >>> izberi_moznost(['jabolko'])
    0
    """

    if len(moznosti) == 0:
        return
    elif len(moznosti) == 1:
        return 0
    else:
        for i, moznost in enumerate(moznosti, 1):
            print('{}) {}'.format(i, moznost))

        st_moznosti = len(moznosti)
        while True:
            izbira = input('Vnesite izbiro > ')
            if not izbira.isdigit():
                print('NAPAKA: vnesti morate število')
            else:
                n = int(izbira)
                if 1 <= n <= st_moznosti:
                    return n - 1
                else:
                    print('NAPAKA: vnesti morate število med 1 in {}!'.format(
                        st_moznosti))
# 1) Kupec
def prikazi_podatke_kupcev():
    id_kupca = izberi_kupca()
    if id_kupca is None:
        print('Noben kupec ne ustreza iskalnemu nizu.')
    else:
        ime, naslov, davcna_stevilka, kontaktna_oseba = modeli.podatki_kupca(id_kupca)

        print('  {}'.format(ime))
        print('  naslov: {}'.format(naslov))
        print('  davcna stevilka: {}'.format(davcna_stevilka))
        print('  kontaktna oseba: {}'.format(kontaktna_oseba))
      

def izberi_kupca():
    niz = input('Vnesite del imena kupcev > ')
    idji_kupcev = modeli.poisci_kupca(niz)
    moznosti = [
        '{} ***{}***'.format(ime, naslov) for _, ime, naslov in modeli.podatki_kupcev(idji_kupcev)
    ]
    izbira = izberi_moznost(moznosti)
    return None if izbira is None else idji_kupcev[izbira]

# 2) Izdelki
def prikazi_podatke_izdelkov():
    id_izdelka = izberi_izdelek()
    if id_izdelka is None:
        print('Noben izdelek ne ustreza iskalnemu nizu.')
    else:
        opis, zaloga, cena, kategorija = modeli.podatki_izdelka(id_izdelka)
        print('  {}'.format(opis))
        print('  zaloga: {}'.format(zaloga))
        print('  cena: {}'.format(cena))
        print('  kategorija izdelka: {}'.format(kategorija[0]))

def izberi_izdelek():
    niz = input('Poiščite svojo uro > ')
    idji_izdelkov = modeli.poisci_izdelek(niz)
    moznosti = [
        '{} ---> {} EUR'.format(opis, cena) for _, opis, cena in modeli.podatki_izdelkov(idji_izdelkov)
    ]
    izbira = izberi_moznost(moznosti)
    return None if izbira is None else idji_izdelkov[izbira]


# 3) Naročila
def prikazi_podatke_narocil():
    id_narocila = izberi_narocilo()
    if id_narocila is None:
        print('Nobeno narocilo ne ustreza iskalnemu nizu.')
    else:
        id_narocilo, datum, rok_placila, kupec, status, izdelki = modeli.podatki_narocila(id_narocila)
        print('  Stevilka narocila {}'.format(id_narocilo))
        print('  datum: {}'.format(datum))
        print('  rok placila: {}'.format(rok_placila))
        print('  kupec: {}'.format(kupec))
        print('  status placila: {}'.format(status))
        print('  Izdelki:')
        for izdelek in izdelki:
            print('         Naziv izdelka: {}'.format(izdelek[0])) # Naziv izdelka povlečen
            print('         Cena izdelka: {}'.format(izdelek[1])) # Naziv izdelka povlečen
            print('         Količina izdelka: {}'.format(izdelek[2])) # Naziv izdelka povlečen
            print('         Popust na izdelek: {}%'.format(izdelek[3]*100)) # Naziv izdelka povlečen





def izberi_narocilo():
    niz = input('Vnesite datum naročila (format: dd/mm/yyyy) > ')
    idji_narocil = modeli.poisci_narocila(niz)
    moznosti = [
        'številka naročila: {} Kupec: {}'.format(id_narocila, kupec) for _, id_narocila, kupec in modeli.podatki_narocil(idji_narocil)
    ]
    izbira = izberi_moznost(moznosti)
    return None if izbira is None else idji_narocil[izbira]




def pokazi_moznosti():
    print(50 * '-')
    izbira = izberi_moznost([
        'prikaži podatke kupca',
        'prikaži podatke o izdelku',
        'prikaži podatke o narocilu',
        # 'dodaj vlogo osebe v filmu',
        # 'prikaži najboljše filme posameznega desetletja',
        # 'dodaj film',
        'izhod',
    ])



    if izbira == 0:
        prikazi_podatke_kupcev()
    elif izbira == 1:
        prikazi_podatke_izdelkov()
    elif izbira == 2:
        prikazi_podatke_narocil()
    # elif izbira == 3:
    #     prikazi_najboljse_filme_desetletja()
    # elif izbira == 4:
    #     dodaj_film()
    else:
        print('Nasvidenje!')
        exit()
        


def main():
    print('Pozdravljeni v trgovini ur!')
    while True:
        pokazi_moznosti()


main()