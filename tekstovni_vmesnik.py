import model 

lojtrice = 20 * '#' + '\n'

def izpis_zmage(igra):
    return lojtrice + 'Čestitke, zmagali ste! Uganili ste besedo {0}!'.format(igra.geslo)

def izpis_poraza(igra):
    return lojtrice + 'Na žalost ste porabili vse poskuse in izgubili igro. Geslo je bilo {0}.'.format(igra.geslo)

def izpis_igre(igra):
    niz = lojtrice 
    niz += igra.pravilni_del_gesla() 
    niz += '\n' + slika(igra)
    niz += '\n' + 'Napačni ugibi: {0}\n'.format(igra.nepravilni_ugibi()) 
    niz += lojtrice[:-1]
    return niz

def slika(igra):
    n = igra.stevilo_napak()
    if n == 0:
        niz = 'Na voljo imate 10 napačnih ugibov.'
    if n == 1:
        niz = '_______'
    if n == 2:
        niz = ' |\n |\n |\n |\n_|______'
    if n == 3:
        niz = ' _____\n |\n |\n |\n |\n_|______'
    if n == 4:
        niz = ' _____\n |/\n |\n |\n |\n_|______'
    if n == 5:
        niz = ' _____\n |/  |\n |\n |\n |\n_|______'
    if n == 6:
        niz = ' _____\n |/  |\n |   o\n |\n |\n_|______'
    if n == 7:
        niz = ' _____\n |/  |\n |   o\n |   |\n |\n_|______'
    if n == 8:
        niz = ' _____\n |/  |\n |   o\n |  /|\n |\n_|______'
    if n == 9:        
        niz = ' _____\n |/  |\n |   o\n |  /|\\\n |\n_|______'
    if n == 10:
        niz = ' _____\n |/  |\n |   o\n |  /|\\\n |  /\n_|______'
    if n == 11:
        niz = ' _____\n |/  |\n |   o\n |  /|\\\n |  / \\\n_|______'
    return niz
    




def izpis_novo():
    if input('Če želite začeti novo igro napišite da. ') == 'da':
        pozeni_vmesnik()

def zahtevaj_vnos():
    a = input('Ugibati želim črko: ')
    if a.isalpha() and len(a) == 1:
        return a
    else:
        print('Ugiba se z natanko eno črko!')
        return zahtevaj_vnos()
    

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
            print(slika(igra))
            print(izpis_poraza(igra))
            break
    izpis_novo()


pozeni_vmesnik()
