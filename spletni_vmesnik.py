import modeli
from bottle import get, template, run, request, post, redirect


def url_ure(id):
    return 'ura/{}/'.format(id)



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

@get('/iskanje/')
def iskanje():
    niz = request.query.opis
    idji_izdekov = modeli.poisci_izdelek(niz)
    filmi = [(id_izdelek, opis, cena, '/film/{}/'.format(id)) for (id_izdelek, opis, cena) in modeli.podatki_izdelkov(idji_izdekov)]
    idji_izdelkov = modeli.poisci_izdelek(niz)
    print(idji_izdelkov)
    return template('rezultat_iskanja', izdelki = modeli.podatki_izdelkov(idji_izdelkov),niz=niz)


@get('/ura/<id_ure:int>/')
def podatki_ure(id_ure):
    opis, zaloga, cena, kategorija = modeli.podatki_izdelka3(id_ure) # TODO dodaj kategorijo
    print(opis,zaloga,cena)
    return template(
        'podatki_ure',
        opis=opis,
        zaloga=zaloga,
        cena=cena,
        kategorija = kategorija,
        
)

@get('/dodaj_uro/')
def dodaj_uro():
   # if not prijavljen_uporabnik():
     #   raise bottle.HTTPError(401)
    kategorije = modeli.mozne_kategorije()
    return template('dodaj_uro',
                    opis="",
                    zaloga="",
                    cena="",
                    kategorije="",
                    vse_kategorije=kategorije,
                    napaka=False)

@post('/dodaj_uro/')
def dodajanje_ure():
    #if not prijavljen_uporabnik():
        #raise bottle.HTTPError(401)
    try:
        print('Zašo u TRY')
        print(request.forms.dict)
        id = modeli.dodaj_uro(opis=request.forms.opis,
                               zaloga=request.forms.zaloga,
                               cena=request.forms.cena,
                               kategorije=request.forms.kategorije)
        
                               
                              # zanri=request.forms.getall('zanri'),
                              
                              # reziserji=request.forms.getall('reziserji'))
    except:
        kategorije = modeli.mozne_kategorije()
        return template('dodaj_uro',
                        opis=request.forms.opis,
                               zaloga=request.forms.zaloga,
                               cena=request.forms.cena,
                               ocena=request.forms.ocena,
                               kategorije=request.forms.kategorije,
                               vse_kategorije=kategorije,
                               napaka=True)
    
    redirect('/ura/{}/'.format(id))


run(reloader=True,debug=True)