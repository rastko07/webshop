import bottle
from bottle import get

@get('/')
def glavna_stran():
    return 'Zdravo'

bottle.run()