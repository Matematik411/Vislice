import random

#konstante
STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'


#glavni razred
class Igra:
    def __init__(self, geslo, crke=[]):
        self.geslo = geslo
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



with open('besede.txt', 'r', encoding='utf-8') as dat:
    bazen_besed = [vrstica.strip().upper()  for vrstica in dat]

def nova_igra():
    return Igra(random.choice(bazen_besed))



    




