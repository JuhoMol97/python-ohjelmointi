import random

def heita_noppa(tahkojen_maara):
    return random.randint(1,tahkojen_maara)

silmaluku = int(input("Anna silmälukujen määrä: "))
while True:
    noppa = heita_noppa(silmaluku)
    print(noppa)
    if noppa == silmaluku:
        break