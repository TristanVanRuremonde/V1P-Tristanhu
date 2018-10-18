import datetime
import csv

bestand = 'inloggers.csv'

while True:

    naam = input("Wat is je achternaam? ")
    if naam == 'einde':
        break
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    with open(bestand, 'a', newline='') as CSV:
        writer = csv.writer(CSV, delimiter=';')
        writer.writerow((voorl, naam, gbdatum, email))




#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file
