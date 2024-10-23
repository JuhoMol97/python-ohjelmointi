class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippusnopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0


auto1 = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus: {auto1.rekisteritunnus}, huippunopeus: {auto1.huippusnopeus}, tämänhetkinen nopeus: {auto1.nopeus}, kuljettu matka: {auto1.kuljettumatka}")