import random

pisteet = int(input("Anna pisteiden määrä: "))

i = 0
kerrat = 0

while i < pisteet:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        kerrat += 1
    i+=1
print(f"piin likiarvo on noin: {kerrat * 4 / pisteet}")