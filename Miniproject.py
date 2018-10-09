import random
import string
import csv
import datetime


lstUniqueNumbers = []


def login():
    try:
        loginkeuze = int(input("Wat wil je doen?: /n 1.Account aanmaken /n 2. Fiets stallen /n 3. fiets ophalen /n 4. informatie opvragen"))
        if loginkeuze == 1:
            gebruikersInformatie()
        elif loginkeuze == 2:
            print('2')
        elif loginkeuze == 3:
            print('3')
        elif loginkeuze == 4:
            print('4')
        print('Error login')
    except ValueError:
        print("Graar een cijfer invullen")

def uniqueNumber():
    print('UniqueNumber')
    'genereert een uniek getal voor de gebruiker'
    uniekNummer = ''
    while True:
        if len(uniekNummer) == 10:
            if uniekNummer in lstUniqueNumbers:
                # exception voor een kans van n/1.200.000.000.000 met n=iterations
                uniekNummer = ''
            else:
                break
        if len(uniekNummer) % 2 == 0:
            uniekNummer += str(random.randrange(0, 10))
        elif len(uniekNummer) % 2 != 0:
            uniekNummer += random.choice(string.ascii_letters)
    lstUniqueNumbers.append(uniekNummer)
    return uniekNummer


def gebruikersInformatie():
    print('Gebruikersinformatie')
    'vraagt gebruiker voor zijn/haar naam'
    voornaamUser = str(input(('Voornaam: ')))
    achternaamUser = str(input('Achternaam: '))
    tussenvoegselUser = str(input('Tussenvoegsel [laat leeg indien je er geen hebt...]: '))
    while True:
        wachtwoordKoppel = str(input('Geef wachtwoord [min. 6 karakters met twee cijfers]: '))
        wachtwoord = ''
        noOfIntsInPass = 0
        for o in wachtwoordKoppel:
            wachtwoord += o
            try:
                int(o)
                noOfIntsInPass += 1
            except ValueError:
                pass
        if len(wachtwoord) > 6 and noOfIntsInPass >= 2:
            break
        else:
            print('Incorrect wachtwoord. Probeer het opnieuw')

    # formatting is moeilijk
    if tussenvoegselUser == '':
        naamUser = voornaamUser + ' ' + achternaamUser
    else:
        naamUser = voornaamUser + ' ' + tussenvoegselUser + ' ' + achternaamUser
        # callt de functie uniqueNumber voor een random string als uniek nummer
    gebruikersNummer = uniqueNumber()
    with open('Gebruikersbestand.csv', 'w', newline='') as CSV:
        writer = csv.writer(CSV, delimiter=';')

        writer.writerow((gebruikersNummer, naamUser, wachtwoord, ''))


def fietsStallen():
    print('fietsenstallen')
    correcteGegevens = False
    huidigeTijd = datetime.datetime.now()
    opgegevenGebruikersnaam = str(input('Geef je unieke code: '))
    opgegevenWachtwoord = str(input('Voer je wachtwoord in: '))
    with open('Gebruikersbestand.csv', 'r') as CSV:
        for o in CSV.readlines():
            print(o.split(';')[0])
            print(o.split(';')[2])
            wachtwoord = o.split(';')[2]
            if opgegevenGebruikersnaam == o.split(';')[0]:
                if wachtwoord == opgegevenWachtwoord:
                    print('Ingelogd')

                    #extra lijn toevoegen  dat zegt gestald = true of false
                    #Waar gestald?

                    correcteGegevens = True
            else:
                print('Iets ging fout. Probeer het opnieuw')
    with open('Stallingsbestand', 'w', newline='') as CSV:
        writer = csv.writer(CSV, delimiter=';')

        if correcteGegevens == True:
            writer.writerow((opgegevenGebruikersnaam, huidigeTijd))


print(uniqueNumber())
gebruikersInformatie()
fietsStallen()