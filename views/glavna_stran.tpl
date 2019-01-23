% rebase('osnova')
<h1 class="title">Dobrodošli v trgovini ur!</h1>
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
   
   
   

   




