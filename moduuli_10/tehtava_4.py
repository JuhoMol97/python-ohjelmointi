import random

class Kilpailu:
    def __init__(self, kilp_nimi, pituus_km, autolista):
        self.kilp_nimi = kilp_nimi
        self.pituus_km = pituus_km
        self.autolista = autolista

    def tunti_kuluu(self):
        for auto in self.autolista:
            kiihdytys = random.randint(-10, 15)
            auto.kiihdyta(kiihdytys)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"Rekisteritunnus:    Huippunopeus:   Nopeus:   Kuljettu matka:")
        for i in self.autolista:
            rektun = i.rekisteritunnus
            huipnop = i.huippunopeus
            nop = i.nopeus
            kuljmatk = i.kuljettumatka
            print(f"{str(rektun):20s}{str(huipnop):16s}{str(nop):10s}{str(kuljmatk):10s}")

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.kuljettumatka >= 10000:
                return True
        return False

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdyta(self, nopeuden_muutos):
        if self.nopeus + nopeuden_muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus + nopeuden_muutos < 0:
            self.nopeus = 0
        else:
            self.nopeus = self.nopeus + nopeuden_muutos

    def kulje(self, tuntimaara):
        self.kuljettumatka += (self.nopeus * tuntimaara)


autolista = []
for i in range(10):
    rektun = "ABC-" + str(i + 1)
    nop = random.randint(100, 200)
    autolista.append(Auto(rektun, nop))

kilpailu = Kilpailu("Suuri Romuralli", 8000, autolista)

tunnit = 0
while True:
    kilpailu.tunti_kuluu()
    if kilpailu.kilpailu_ohi():
        break
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()
kilpailu.tulosta_tilanne()
print(f"Kuluneet tunnit: {tunnit}")