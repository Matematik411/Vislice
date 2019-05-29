import bottle
import model

DATOTEKA_S_STANJEM = 'stanje.json'
SKRIVNOST = 'skrivnost'
DATOTEKA_BESED = 'besede.txt'
vislice = model.Vislice(DATOTEKA_S_STANJEM, DATOTEKA_BESED)



@bottle.get("/")
def index():
    return bottle.template('index.tpl')





@bottle.post("/nova_igra/")
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie("id_igre", id_igre, secret=SKRIVNOST, path = "/")
    bottle.redirect("/igra/")

@bottle.get("/igra/")
def pokazi_igro():
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNOST)
    return bottle.template('igra.tpl',
    igra=vislice.igre[id_igre][0],
    id_igre=id_igre,
    poskus = vislice.igre[id_igre][1]
    )

@bottle.post("/igra/")
def ugibaj():
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNOST)
    crka_ugiba = bottle.request.forms.getunicode("crka")
    if not crka_ugiba.isalpha() or len(crka_ugiba) > 1:
        bottle.redirect("/napaka/")
    vislice.ugibaj(id_igre, crka_ugiba)
    bottle.redirect("/igra/")

@bottle.get("/napaka/")
def napaka():
    return bottle.template('napaka.tpl')



@bottle.get("/img/<picture>/")
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')









bottle.run(reloader=True, debug=True)