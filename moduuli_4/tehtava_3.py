syote = input("Anna luku: ")
luku = int(syote)
min_luku = luku
max_luku = luku

while syote != "":
    luku = int(syote)
    if luku < min_luku:
        min_luku = luku
    if luku > max_luku:
        max_luku = luku
    syote = input("Anna luku: ")

print(f"pienin luku oli {min_luku}")
print(f"suurin luku oli {max_luku}")


# lista = []

# luku = int(input("Anna luku: "))
# while luku > 0:
#     lista.append(luku)
#     luku = int(input("Anna luku: "))

# print(lista)
# print(min(lista))
# print(max(lista))