% rebase('osnova')
<h1 class = "title">Ure v izbrani kategoriji {{kategorija}}<h1>
<ul>
% for opis, kolicina, cena in ure:
    <li>
             Naziv: <strong>{{ opis }},</strong>
             Količina: {{ kolicina }},
             Cena: {{ cena }} €

    </li>
% end
</ul>