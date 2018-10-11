import random
import string
import csv
import datetime


lstUniqueNumbers = []


def login_menu():
    try:
        loginkeuze = int(input("Wat wil je doen?: \n 1.Inloggen \n 2. Registratie: "))
        if loginkeuze == 1:
            inloggen()
        elif loginkeuze == 2:
            registreren()

        else:
            print('Error login')
    except ValueError:
        print("Graag een cijfer invullen")

def inloggen():
    opgegevenGebruikersnaam = str(input('Geef je unieke code: '))
    opgegevenWachtwoord = str(input('Voer je wachtwoord in: '))
    with open('Gebruikersbestand.csv', 'r') as CSV:
        for o in CSV.readlines():
            print(o.split(';')[0])
            print(o.split(';')[2])
            wachtwoord = o.split(';')[2]
            if opgegevenGebruikersnaam == o.split(';')[0]:
                if wachtwoord == opgegevenWachtwoord:
                    ingelogd()


def ingelogd():
    try:
        loginkeuze = int(input("Wat wil je doen?: \n 1. Fiets stallen \n 2. fiets ophalen \n 3. informatie opvragen \n Keuze: "))
        if loginkeuze == 1:
            openStalling()
        elif loginkeuze == 2:
            fietsOphalen()
        elif loginkeuze == 3:
            algemeneInformatie()
        else:
            print('Error login')
    except ValueError:
        print("Graag een cijfer invullen")



def uniqueNumber():
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


def registreren():
    'vraagt gebruiker voor zijn/haar naam'
    voornaamUser = str(input('Voornaam: '))
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
        if len(wachtwoord) >= 6 and noOfIntsInPass >= 2:
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
    with open('Gebruikersbestand.csv', 'a', newline='') as CSV:
        writer = csv.writer(CSV, delimiter=';')

        writer.writerow((gebruikersNummer, naamUser, wachtwoord, ''))
def login():
    lstGebruikersGegevens = []
    with open('Gebruikersbestand.csv', 'r') as CSV:
            opgegevenGebruikersnaam = str(input('Geef je unieke code: '))
            opgegevenWachtwoord = str(input('Voer je wachtwoord in: '))
            for o in CSV.readlines():
                wachtwoord = o.split(';')[2]
                if opgegevenGebruikersnaam == o.split(';')[0]:
                    if wachtwoord == opgegevenWachtwoord:
                        print('Ingelogd')
                        lstGebruikersGegevens = o
                        break
                else:
                    print('Iets ging fout. Probeer het opnieuw')
                    break
    return lstGebruikersGegevens

def openStalling(naam):
    huidigeTijd = datetime.datetime.now()
    with open('Stallingsbestand.csv', 'a', newline='') as CSV:
        writer = csv.writer(CSV, delimiter=';')
        writer.writerow((naam, huidigeTijd))


def algemeneInformatie():
    huidigeTijd = datetime.datetime.now()
    counterUsersLastHour = 0
    with open('Gebruikersbestand.csv', 'r', newline='') as CSV:
        hoeveelheidGebruikers = len(CSV.readlines())
    with open('Stallingsbestand.csv', 'r', newline='') as CSV:
        for o in CSV.readlines():
            lijn = o.split(';')[1]
            huidigUur = str(huidigeTijd).split(':')[0]
            if huidigUur == lijn.split(':')[0]:
                counterUsersLastHour += 1
    print('Aantal gebruikers van dit programma: ', hoeveelheidGebruikers)
    print('Aantal gebruikers ingelogd in het laatste uur: ', counterUsersLastHour)


def persoonlijkeInformatie():
    lstGebruikersGegevens = login()
    huidigeTijd = datetime.datetime.now()
    print('Welkom ', lstGebruikersGegevens.split(';')[1])
    print('Het is nu: ', huidigeTijd)
def fietsOphalen():
    correcteGegevens = False
    lstGebruikersGegevens = login()
    with open('Gebruikersbestand.csv', 'r') as CSV:
        for o in CSV.readlines():
            while correcteGegevens == False:
                if o.split(';')[0] == lstGebruikersGegevens.split(';')[0]:
                    print('Verhaaltje over ophalen van een fiets, hoezee.')
                    correcteGegevens = True
                    break

login_menu()
