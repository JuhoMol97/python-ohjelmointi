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


auto1 = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus: {auto1.rekisteritunnus}, huippunopeus: {auto1.huippunopeus}, tämänhetkinen nopeus: {auto1.nopeus}, kuljettu matka: {auto1.kuljettumatka}")
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"Auton nopeus on {auto1.nopeus}")
auto1.kiihdyta(-200)
print(f"Auton nopeus on {auto1.nopeus}")