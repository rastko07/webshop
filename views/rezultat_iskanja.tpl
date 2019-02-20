% rebase('osnova')

Poizvedba za niz '{{niz}}' je vrnila naslednje ure:

<ul>

    % for id_ure,opis,cena in izdelki:
        
        <li>
            <a href="/ura/{{ id_ure }}/">
                <strong>{{opis}}</strong>,{{cena}} €
            </a>
        </li>
% end
</ul>