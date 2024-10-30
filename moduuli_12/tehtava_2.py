import requests

apikey = "7a5b4d3b55d36e94aca154851550e478"

def hae_koordinaatit(kaupunki,apikey):
    lokaatio = f"http://api.openweathermap.org/geo/1.0/direct?q={kaupunki}&limit=5&appid={apikey}"
    kaupunki_pyynto = requests.get(lokaatio).json()[0]
    return kaupunki_pyynto["lon"], kaupunki_pyynto["lat"]

def get_weather(kaupunki, apikey):
    lon, lat = hae_koordinaatit(kaupunki, apikey)
    saatila_pyynto = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}&units=metric"
    return requests.get(saatila_pyynto).json()

def hae_saatiedot():
    kaupunki = input("Anna kaupunki: ")
    saatila = get_weather(kaupunki, apikey)
    saatila_desc = saatila["weather"][0]["description"]
    saatila_celsius = saatila["main"]["temp"]
    print(f"Säätila: {saatila_desc} \nLämpotila: {saatila_celsius}C")

hae_saatiedot()