import baza
import sqlite3

conn = sqlite3.connect('trgovina5.db')
baza.ustvari_bazo_ce_ne_obstaja(conn)
conn.execute('PRAGMA foreign_keys = ON')
conn.execute("PRAGMA encoding = 'UTF-8'")

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