import math

def pizzaneliometri(pizzan_halkaisija, pizzan_hinta):
    pizzan_pinta_ala = math.pi * (pizzan_halkaisija / 2) ** 2
    euroina_per_neliometri = pizzan_hinta / pizzan_pinta_ala
    return euroina_per_neliometri

pizza_1_halkaisija = float(input("Anna pizzan 1. halkaisija metreinä: "))
pizza_1_hinta = float(input("Anna pizzan 1. hinta: "))
pizza_2_halkaisija = float(input("Anna pizzan 2. halkaisija metreinä: "))
pizza_2_hinta = float(input("Anna pizzan 2. hinta: "))

pizza_1_arvo = pizzaneliometri(pizza_1_halkaisija, pizza_1_hinta)
pizza_2_arvo = pizzaneliometri(pizza_2_halkaisija, pizza_2_hinta)

print(f"Pizzan 1. hinta neliömetreinä on {pizza_1_arvo:.2f} €/m^2 ja pizzan 2. on {pizza_2_arvo:.2f} €/m^2")

if pizza_1_arvo < pizza_2_arvo:
    print(f"Pizza 1. antaa paremman vastineen rahallesi.")
elif pizza_1_arvo > pizza_2_arvo:
    print(f"Pizza 2. antaa paremman vastineen rahallesi.")
else:
    print("Pizzat antavat yhtä hyvän arvon rahallesi.")