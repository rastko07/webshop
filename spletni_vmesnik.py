import modeli
from bottle import get, template, run

@get('/')
def glavna_stran():
    
    kategorije = [
        (kategorija, '/kategorije/{}/'.format(id_kategorije))
        for kategorija, id_kategorije, in modeli.mozne_kategorije()
    ]
    return template(
        'glavna_stran',
        kategorije = kategorije)


@get('/kategorije/<id_kategorije:int>/')
def kategorija_stran(id_kategorije):
    ure =  modeli.mozne_ure(id_kategorije)
    kategorija, = modeli.trenutna_kategorija(id_kategorije)
    return template(
        'kategorije_stran',
        ure = ure,
        kategorija = kategorija)

@get('/iskanje/<niz>')
def iskanje(niz):
    idji_izdelkov = modeli.poisci_izdelek(niz)
    print(idji_izdelkov)
    return template('rezultat_iskanja', izdelki = modeli.podatki_izdelkov(idji_izdelkov),niz=niz)


run(reloader=True,debug=True)