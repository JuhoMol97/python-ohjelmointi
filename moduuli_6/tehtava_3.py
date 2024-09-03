def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    gallonamaara = int(input("Anna bensiinin määrä galloneina: "))
    if gallonamaara < 0:
        break
    litrat = gallonat_litroiksi(gallonamaara)
    print(f"Antamasi gallonamäärä litroina on {litrat} litraa")