% rebase('osnova')

% if napaka:
<p>Prišlo je do napake!</p>
% end

<form method="post">
Opis: <input type="text" name="opis" value="{{opis}}" /><br />
Zaloga: <input type="text" name="zaloga" value="{{zaloga}}" /><br />
Cena: <input type="text" name="cena" value="{{cena}}" /><br />

Kategorije: <select name="kategorije">
% for  ime, id_kategorija in vse_kategorije:
    <option value="{{id_kategorija}}" {{'selected' if str(id_kategorija) in kategorije else ''}}>{{ime}}</option>
% end
</select>
<br />


<input type="submit" value="Dodaj uro">
</form>