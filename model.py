import random
import json

#konstante
STEVILO_DOVOLJENIH_NAPAK = 9
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'
ZACETEK = 'S'




#glavni razred
class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke

    
    def napacne_crke(self):
        return [a for a in self.crke if a not in self.geslo]
        
    def pravilne_crke(self):
        return [a for a in self.crke if a in self.geslo]
    
    def stevilo_napak(self):
        return len(self.napacne_crke())
    

    def zmaga(self):
        for a in self.geslo:
            if a not in self.crke:
                return False
        return True

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for a in self.geslo:
            if a in self.pravilne_crke():
                niz += a
            else:
                niz += '_'
            niz += ' '
        return niz
    
    def nepravilni_ugibi(self):
        niz = ''
        for a in self.napacne_crke():
            niz += a + ' '
        return niz[:-1]
    
    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke += [crka]
        if crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            return NAPACNA_CRKA






#test = 'požrtvovalnost'.upper()
#testne = ['A', 'B', 'E', 'T']
#zmaga = [a for a in test]
#igra = Igra(test, testne)
#print(igra.napacne_crke())
#print(igra.pravilne_crke())
#print(igra.zmaga())
#print(igra.pravilni_del_gesla())
#zmagovalna = Igra(test, zmaga)
#print(zmagovalna.zmaga())






#nadzor iger
class Vislice:

    def __init__(self, datoteka_s_stanjem, datoteka_besed):
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.datoteka_besed = datoteka_besed

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()
        id_igre = self.prost_id_igre()
        with open(self.datoteka_besed, 'r', encoding='utf-8') as dat:
            bazen_besed = [vrstica.strip().upper()  for vrstica in dat]
        igra = Igra(random.choice(bazen_besed))
        self.igre[id_igre] = (igra, ZACETEK)
        self.zapisi_igre_v_datoteko()
        return id_igre

    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()
        igra = self.igre[id_igre][0]
        novo_stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, novo_stanje)
        self.zapisi_igre_v_datoteko()

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as dat:
            igre = json.load(dat)
            self.igre = {int(id_igre): (
                                Igra(igre[id_igre]['geslo'], igre[id_igre]['crke']),
                                igre[id_igre]['poskus']
                                )
                for id_igre in igre
            }


    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as dat:
            igre = ({id_igre: {'geslo': igra.geslo, 'crke': igra.crke, 'poskus': poskus}
                    for id_igre, (igra, poskus) in self.igre.items()})
            json.dump(igre, dat)



