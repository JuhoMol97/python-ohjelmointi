def parittomat_pois(koko_lista):
    parittomien_lista = []
    for luku in koko_lista:
        if luku % 2 == 0:
            parittomien_lista.append(luku)
    return parittomien_lista

lista = []
while True:
    luku = int(input("Anna luku(nolla lopettaa): "))
    if luku == 0:
        break
    lista.append(luku)

print(lista)
print(parittomat_pois(lista))