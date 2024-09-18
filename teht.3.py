lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1. Syötä uusi lentoasema")
    print("2. Hae lentoasema")
    print("3. Lopeta")

    valinta = input("Syötä valinta (1-3): ")

    if valinta == "1":
        icao = input("Syötä lentoaseman ICAO-koodi: ").upper()
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} (ICAO: {icao}) tallennettu.")

    elif valinta == "2":
        icao = input("Syötä haettavan lentoaseman ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao]}")
        else:
            print(f"Lentoasemaa ICAO-koodilla {icao} ei löytynyt.")

    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")
