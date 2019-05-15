import model 

lojtrice = 20 * '#' + '\n'

def izpis_zmage(igra):
    return lojtrice + 'Čestitke, zmagali ste! Uganili ste besedo {0}!'.format(igra.geslo)

def izpis_poraza(igra):
    return lojtrice + 'Na žalost ste porabili vse poskuse in izgubili igro. Geslo je bilo {0}.'.format(igra.geslo)

def izpis_igre(igra):
    return lojtrice + igra.pravilni_del_gesla() + '\n' + 'Preostalo število poskusov: {0}\nNapačni ugibi: {1}\n'.format(model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1, igra.nepravilni_ugibi()) + lojtrice[:-1]


def zahtevaj_vnos():
    return input('Ugibati želim črko: ')

def pozeni_vmesnik():
    igra = model.nova_igra()

    while True:
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        igra.ugibaj(poskus)

        if igra.zmaga():
            print(izpis_zmage(igra))
            break
        
        if igra.poraz():
            print(izpis_poraza(igra))
            break


pozeni_vmesnik()
