import math

def kuukausi_vuodenajaksi(kk):
    vuodenaika = math.floor(kk/3)
    if vuodenaika == 0:
        vuodenaika += 4
    return vuodenaika

vuodenajat = ("kevät","kesä","syksy","talvi")

kuukausi = int(input("Anna kuukauden numero: "))

oikea_vuodenaika = kuukausi_vuodenajaksi(kuukausi)

print(vuodenajat[oikea_vuodenaika-1])