class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_maara = hissien_maara
        self.hissilista = []
        for i in range(hissien_maara):
            self.hissilista.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissia(self, hissin_numero, kerros):
        self.hissilista[hissin_numero - 1].siirry_kerrokseen(kerros)


class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, haluttu_kerros):
        while self.kerros != haluttu_kerros:
            if self.kerros < haluttu_kerros:
                if self.kerros == self.ylin_kerros:
                    print(f"Saavuit ylimpään kerrokseen, joten et voi mennä ylemmäs.")
                    break
                self.kerros_ylos()
            if self.kerros > haluttu_kerros:
                if self.kerros == self.alin_kerros:
                    print(f"Saavuit alimpaan kerrokseen, joten et voi mennä alemmas.")
                    break
                self.kerros_alas()

    def kerros_ylos(self):
        self.kerros += 1
        print(f"Olet nyt kerroksessa {self.kerros}.")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Olet nyt kerroksessa {self.kerros}.")


talo = Talo(1, 10, 3)
talo.aja_hissia(1, 7)
talo.aja_hissia(1, 1)
talo.aja_hissia(3, 100)