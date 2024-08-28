import random

noppien_maara = int(input("Anna noppien määrä: "))
summa = 0

for i in range(0, noppien_maara):
    silmaluku = random.randint(1,6)
    summa += silmaluku
    print(silmaluku)
print(f"Silmälukujen summa on {summa}")