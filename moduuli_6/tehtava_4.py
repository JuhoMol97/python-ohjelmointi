def listan_lukujen_summa(lukulista):
    summa = 0
    for listanluku in lukulista:
        summa += listanluku
    return summa

lista_lukuja = []

while True:
    luku = int(input("Anna luku(nolla lopettaa): "))
    if luku == 0:
        break
    lista_lukuja.append(luku)

lukujen_summa = listan_lukujen_summa(lista_lukuja)
print(f"Antamiesi lukujen summa on {lukujen_summa}")