<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello Bulma!</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
  </head>
  <body>
          
       <section class="hero is-big is-primary is-bold">
            <div class="hero-body">
            <div class="container">
              <nav class = "navbar" role = "navigation">
                <div class = "navbar-brand">
                  <a class = "navbar-item" href = "/">
                   <i class = "fas fa-home" style = "font-size: 3em;"></i>
                    <p style = "font-size: 2em;">DOMOV</p>
                  </a>
                </div>
              </nav>
            </div>
            </div>
       </section>
  <section class="section">
    <div class="container">
     {{!base}}    
    </div>
    %if get('prijavljen',False):
      <p> <a href= "http://www.google.com/">Dodaj narocilo</a>
    %end
  </section>
  <br></br><br></br><br></br><br></br>
  <footer class="footer">
  <div class="content has-text-centered">
    <p>
      &copy Rastko Veriš, Borna Kavcic 2019
    </p>
  </div>
</footer>
  </body>
</html>
   
   
   
   

   




