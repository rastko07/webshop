% rebase('osnova')
<h1 class = "title">Ure v izbrani kategoriji {{kategorija}}<h1>
<ul>
% for id_ure, opis, kolicina, cena in ure:
    <li>
             <a href="/ura/{{ id_ure }}/">
             Naziv: <strong>{{ opis }},</strong>
             Količina: {{ kolicina }},
             Cena: {{ cena }} €</a>

    </li>
% end
</ul>