oikea_username = "python"
oikea_password = "rules"

yritykset = 0
kirjautuminen_onnistui = False

while kirjautuminen_onnistui == False:
    annettu_username = input("Anna käyttäjätunnuksesi: ")
    annettu_password = input("Anna salasanasi: ")
    if oikea_username == annettu_username and oikea_password == annettu_password:
        print("Tervetuloa!")
        kirjautuminen_onnistui = True
    else:
        print("Kirjautumistiedoissasi oli virhe")
        if yritykset >= 4:
            print("Pääsy evätty")
            break
    yritykset += 1
