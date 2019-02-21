% rebase('osnova')
<h1 class="title">Dobrodošli v trgovini ur!</h1>

<form action="iskanje/" method="get">
<input type="text" name="opis" value="" />
<input type="submit" value="Išči">
</form>


<ul>
% for kategorija, url in kategorije:
    <li>
        <a href="{{ url }}">
            <div class="column notification is-primary">Poglejte ure iz kategorije {{ kategorija }}</div>
        </a>
    </li>
% end

% if get('prijavljen', False):
    <li><a href="dodaj_uro/">Dodaj uro</a></li>
    <li>
        <a href="odjava/">Odjavi se</a>
    </li>
% end
</ul>
 </div>
  </section>

 


% if not get('prijavljen', False):
<form action="prijava/" method="post">
<input type="text" name="uporabnisko_ime" value="" />
<input type="password" name="geslo" value="" />
<input type="submit" value="Prijavi se">
</form>
<form action="registracija/" method="post">
<input type="text" name="uporabnisko_ime" value="" />
<input type="password" name="geslo" value="" />
<input type="submit" value="Registriraj se">
</form>
% end
   
   

   




