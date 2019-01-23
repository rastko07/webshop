% rebase('osnova')

Poizvedba za niz '{{niz}}' je vrnila naslednje ure:

<ul>

    % for _,opis,cena in izdelki:
        <li><strong>{{opis}}</strong>,{{cena}} €</li>
% end
</ul>