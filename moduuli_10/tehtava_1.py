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


hissi = Hissi(1, 9)
hissi.siirry_kerrokseen(100)
hissi.siirry_kerrokseen(0)