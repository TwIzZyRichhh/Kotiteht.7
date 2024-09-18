vuodenaika = ("Kesä", "Syksy", "Talvi", "Kevät")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-4): "))
vuodenajat = vuodenaika[järjestysnumero-1]
print (f"{järjestysnumero}. vuodenaika on {vuodenajat}.")