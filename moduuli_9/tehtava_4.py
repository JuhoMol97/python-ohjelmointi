import random

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

kilpailu_paalla = True
while kilpailu_paalla:
    for auto in autolista:
        kiihdytys = random.randint(-10, 15)
        auto.kiihdyta(kiihdytys)
        auto.kulje(1)

    for auto in autolista:
        if auto.kuljettumatka >= 10000:
            kilpailu_paalla = False

print(f"Rekisteritunnus:    Huippunopeus:   Nopeus:   Kuljettu matka:")
for i in autolista:
    rektun = i.rekisteritunnus
    huipnop = i.huippunopeus
    nop = i.nopeus
    kuljmatk = i.kuljettumatka

    print(f"{str(rektun):20s}{str(huipnop):16s}{str(nop):10s}{str(kuljmatk):10s}")