leiviskat_maara = float(input("Anna leiviskat: "))
naulat_maara = float(input("Anna naulat: "))
luoti_maara = float(input("Anna luodit: "))

luoti_paino = 13.3
naulat_paino = 13.3*32
leiviskat_paino = 13.3*32*20
paino_yhteensa = leiviskat_paino * leiviskat_maara + naulat_paino * naulat_maara + luoti_paino * luoti_maara
paino_kg = paino_yhteensa // 1000
paino_g = paino_yhteensa - paino_kg*1000

print(f"Massa nykymittojen mukaan: {paino_kg:.0f} kg ja {paino_g:.2f} g")