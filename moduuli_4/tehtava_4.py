import random

oikea_luku = random.randint(1, 10)
annettu_luku = int(input("Anna luku 1-10 välillä: "))

while annettu_luku != oikea_luku:
    if annettu_luku < oikea_luku:
        print("Arvauksesi oli liian pieni")
    if annettu_luku > oikea_luku:
        print("Arvauksesi oli liian suuri")
    annettu_luku = int(input("Anna uusi luku 1-10 välillä: "))
print("Oikein!")