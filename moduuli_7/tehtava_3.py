lentoasemat = {
    "EFHK":"Helsinki-Vantaa lentoasema",
    "EBBR":"Brysselin lentokenttä",
    "EDDB":"Berliinin lentokenttä",
    "EDDF":"Frankfurtin lentokenttä",
    "EDDH":"Hampurin lentokenttä",
}

while True:
    syote = input("Anna numero että haluatko lisätä(1) lentoaseman, hakea(2) lentoasemaa vai lopettaa(3): ")
    if syote == "1":
        lisays_icao = input("Anna uuden lentokentän ICAO-koodi: ")
        lisays_nimi = input("Anna lisättävän lentokentän nimi: ")
        lentoasemat[lisays_icao] = lisays_nimi
        print("Lentokenttä lisätty onnistuneesti hakemistoon!")
    elif syote == "2":
        haku_icao = input("Anna haettavan lentokentän ICAO-koodi: ")
        if haku_icao in lentoasemat:
            print(f"{haku_icao}: {lentoasemat[haku_icao]}")
        else:
            print("Kyseisellä haulla ei löytynyt yhtään tulosta.")
    elif syote == "3":
        print("Kiitos käytöstä!")
        break
    else:
        print("Virheellinen syöte")