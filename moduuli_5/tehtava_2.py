lista = []
kysely_kaynnissa = True

while kysely_kaynnissa == True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        kysely_kaynnissa = False
        continue
    lista.append(int(syote))

lista.sort(reverse=True)
print(lista[0:5])