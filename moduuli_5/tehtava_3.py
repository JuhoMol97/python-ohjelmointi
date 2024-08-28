luku = int(input("Anna luku: "))
alkuluku = True

for i in range(2, luku-1):
    if luku % i == 0:
        alkuluku = False

if alkuluku == True:
    print("Antamasi luku on alkuluku!")
else:
    print("Antamasi luku ei ole alkuluku")