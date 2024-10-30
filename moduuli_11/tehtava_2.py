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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti_kilowattitunteina):
        self.akkukapasiteetti_kilowattitunteina = akkukapasiteetti_kilowattitunteina
        super().__init__(rekisteritunnus, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki_litroina):
        self.bensatankki_litroina = bensatankki_litroina
        super().__init__(rekisteritunnus, huippunopeus)


auto1 = Sähköauto("ABC-15", 180, 52.5)
auto2 = Polttomoottoriauto("ACD-123", 165, 32.3)

auto1.kiihdyta(40)
auto2.kiihdyta(150)

auto1.kulje(3)
auto2.kulje(3)

print(f"Sähköauton matkamittarilukema: {auto1.kuljettumatka} km")
print(f"Polttomoottoriauton mittarilukema: {auto2.kuljettumatka} km")