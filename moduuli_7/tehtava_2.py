nimilista = set()

while True:
    nimi = input("Anna nimi(tyhjä lopettaa): ")
    if nimi == "":
        break
    elif nimi in nimilista:
        print("Aiemmin syötetty nimi")
    else:
        nimilista.add(nimi)
        print("Uusi nimi")

print(nimilista)
for i in nimilista:
    print(i)