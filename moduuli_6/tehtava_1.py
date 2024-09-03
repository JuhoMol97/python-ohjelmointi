import random

def heita_noppa():
    return random.randint(1,6)

while True:
    noppa = heita_noppa()
    print(noppa)
    if noppa == 6:
        break