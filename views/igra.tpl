% import model
% rebase ('base.tpl', title = 'Vislice')

  <h1>Vislice</h1>

  <blockquote>
    Igrate igro vislice.
    Veliko sreče in veselja!
  </blockquote>

  <h2>{{igra.pravilni_del_gesla()}}</h2> 


  Nepravilne črke: {{igra.nepravilni_ugibi()}} <br>

  % preostali = model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1
  Število preostalih poskusov: {{preostali}}
  
  <img src="/img/{{igra.stevilo_napak()}}.jpg/" alt="obesanje">





% if poskus == model.ZMAGA:
    <h2>ZMAGA!</h2>
    <form action="/nova_igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>



% elif poskus == model.PORAZ:
    <h2>PORAZ!</h2>
    Pravilno geslo je {{igra.geslo}}.
    <form action="/nova_igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>



% else:
    <form action="/igra/" method="post">
        Črka: <input type="text" name="crka">        
        <button type="submit">Ugibam</button>
    </form>
% end

