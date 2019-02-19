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
            Poglejte ure iz kategorije {{ kategorija }}
        </a>
    </li>
% end
</ul>
 </div>
  </section>
   
   
   

   




