import random
import string
import csv
import datetime


lstUniqueNumbers = []
lstGebruikersGegevens = [0,0,0]
lstHuidigeStatus = [[]]
aantalStallingen = 50
huidigeTijd = ''
huidigestatus = ''


def uniqueNumber():
    'genereert een uniek getal voor de gebruiker'
    uniekNummer = ''
    while True:
        uniekNummer = uniekNummer.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
        if uniekNummer in lstUniqueNumbers:
            # exception voor een kans van n/839.299.365.868.340.224 met n=users
            uniekNummer = ''
        else:
            break
    # Moet nog uit de while loop kunnen gaan
    lstUniqueNumbers.append(uniekNummer)
    print(uniekNummer)
    return uniekNummer


def registreren(voornaam, tussenvoegsel, achternaam, wachtwoordPara):
    'vraagt gebruiker voor zijn/haar naam evenals wachtwoord'
    gebruikersNummer = ''
    wachtwoord = ''
    noOfIntsInPass = 0
    for o in wachtwoordPara:
        wachtwoord += o
        try:
            int(o)
            noOfIntsInPass += 1
        except ValueError:
            pass
    while True:
        if len(wachtwoord) >= 6 and noOfIntsInPass >= 2:
            geldigWachtwoord = True
            break
        else:
            geldigWachtwoord = False
            break

    # formatting is moeilijk
    if tussenvoegsel == '':
        naamUser = voornaam + ' ' + achternaam
    else:
        naamUser = voornaam + ' ' + tussenvoegsel + ' ' + achternaam
        # callt de functie uniqueNumber voor een random string als uniek nummer
    if naamUser != "" and geldigWachtwoord == True:
        gebruikersNummer = uniqueNumber()
        with open('Gebruikersbestand.csv', 'a', newline='') as CSV:
            writer = csv.writer(CSV, delimiter=';')

            writer.writerow((gebruikersNummer, naamUser, wachtwoord, ''))
            CSV.close()
    return gebruikersNummer


def logineenmalig(unicode, wachtwooord):
    'laat de gebruiker inloggen'
    ingelogd = False
    with open('Gebruikersbestand.csv', 'r') as CSV:
            for o in CSV.readlines():
                if unicode == o.split(';')[0]:
                    if o.split(';')[2] == wachtwooord:
                        global lstGebruikersGegevens
                        lstGebruikersGegevens = o
                        ingelogd = True
                        break
                else:
                    continue
    CSV.close()
    return ingelogd


def openStalling(unicode):
    'opent de stalling aan de hand van de unieke code'
    laatstestatus = ''
    concatenatedStringStatus = ''
    lstStallingsbestand = []
    global lstHuidigeStatus, huidigeTijd, tijdInStallingGegaan
    huidigeTijd = datetime.datetime.now()

    with open('Stallingsbestand.csv', 'r') as CSV:
        for o in CSV.readlines():
            lstStallingsbestand.append(o)
            if o.split(';')[0] == unicode:  # Checkt of de user al in het stalbestand zit
                if o.split(';')[2] == 'uit stalling' or o.split(';')[2] == 'in stalling':
                    concatenatedStringStatus += (o.split(';')[2] + " ")
                    continue
    CSV.close()
    lstJuisteStallingsbestand = []

    for e in lstStallingsbestand:  # filtert onjuiste unicodes en geeft juiste door aan nieuwe list
        if e.split(';')[0] == unicode:
            lstJuisteStallingsbestand.append(e)
    # selecteer de laatste index...
    if len(lstJuisteStallingsbestand) == 1:
        laatstestatus = lstJuisteStallingsbestand[0]
        laatstestatus = str(laatstestatus).split(';')[2]
    elif len(lstJuisteStallingsbestand) > 1:
        laatstestatus = lstJuisteStallingsbestand[-1]
        laatstestatus = str(laatstestatus).split(';')[2]
    elif len(lstJuisteStallingsbestand) == 0:
        laatstestatus = ''
    else:
        return False
    if laatstestatus == 'uit stalling' or laatstestatus == '':
        with open('Stallingsbestand.csv', 'a', newline='') as CSV2:
            writer = csv.writer(CSV2, delimiter=';')
            writer.writerow((unicode, huidigeTijd, 'in stalling', ''))
            tijdInStallingGegaan = str(huidigeTijd)
        CSV2.close()
        return True
    else:
        return False



def algemeneInformatie():
    'returnt het aantal beschikbare stallingen'
    beschikbareStallingen = aantalStallingen - len(lstUniqueNumbers)
    return beschikbareStallingen


def tijduitfunctie(unicode):
    'haalt de tijd uit het stallingsbestand'
    global tijdInStallingGegaan, tijdOpgehaald
    tijdOpgehaald = ''
    tijdInStallingGegaan = ''
    with open('Stallingsbestand.csv', 'r') as CSV:
        for o in CSV.readlines():
            if o.split(';')[0] == unicode:  # Checkt of de user al in het stalbestand zit
                if o.split(';')[2] == 'uit stalling':
                    tijdOpgehaald = o.split(';')[1]
                elif o.split(';')[2] == 'in stalling':
                    tijdInStallingGegaan = o.split(';')[1]
            else:
                pass
        if tijdOpgehaald == '' or tijdInStallingGegaan == '':
            return ''
    CSV.close()


def persoonlijkeInformatie(unicode):
    'laat de gebruiker zien hoe lang hij/zij een fiets gestald heeft gehad'
    global tijdOpgehaald, tijdInStallingGegaan, huidigeTijd
    huidigeTijd = datetime.datetime.now()
    tijduit = tijduitfunctie(unicode)
    if tijduit != '':
        tijdStalling = str(tijdInStallingGegaan).split('.')[0] # error?
        tijdStalling = tijdStalling.split(' ')[1]
        tijdOpgehaald = str(tijdOpgehaald).split('.')[0]
        tijdOpgehaald = tijdOpgehaald.split(' ')[1]
        FMT = '%H:%M:%S'
        if tijdStalling < tijdOpgehaald:
            tdelta = datetime.datetime.strptime(tijdOpgehaald, FMT) - datetime.datetime.strptime(tijdStalling, FMT)
            return tdelta
        else:
            return "Daar ging wat fout in de volgorde"
    else:
        return "Een van de tijden (of beiden) is/zijn leeg"


def fietsOphalen(unicode):
    'laat de gebruiker de fiets ophalen'
    laatstestatus = ''
    concatenatedStringStatus = ''
    lstStallingsbestand = []
    global lstHuidigeStatus, huidigeTijd, tijdInStallingGegaan
    huidigeTijd = datetime.datetime.now()

    with open('Stallingsbestand.csv', 'r') as CSV:
        for o in CSV.readlines():
            lstStallingsbestand.append(o)
            if o.split(';')[0] == unicode:  # Checkt of de user al in het stalbestand zit
                if o.split(';')[2] == 'in stalling' or o.split(';')[2] == 'uit stalling':
                    concatenatedStringStatus += (o.split(';')[2] + " ")
                    continue
    CSV.close()
    lstJuisteStallingsbestand = []

    for e in lstStallingsbestand:  # filtert onjuiste unicodes en geeft juiste door aan nieuwe list
        if e.split(';')[0] == unicode:
            lstJuisteStallingsbestand.append(e)
    # selecteer de laatste index...
    if len(lstJuisteStallingsbestand) == 1:
        laatstestatus = lstJuisteStallingsbestand[0]
        laatstestatus = str(laatstestatus).split(';')[2]
    elif len(lstJuisteStallingsbestand) > 1:
        laatstestatus = lstJuisteStallingsbestand[-1]
        laatstestatus = str(laatstestatus).split(';')[2]
    elif len(lstJuisteStallingsbestand) == 0:
        return False
    else:
        return False
    if laatstestatus == 'in stalling':
        with open('Stallingsbestand.csv', 'a', newline='') as CSV2:
            writer = csv.writer(CSV2, delimiter=';')
            writer.writerow((unicode, huidigeTijd, 'uit stalling', ''))
            tijdInStallingGegaan = str(huidigeTijd)
        CSV2.close()
        return True
    else:
        return False


def returnUsername(input):
    'returnt gebruikersgegevens'
    if input == "unicode":
        return lstGebruikersGegevens[0]
    elif input == "username":
        return lstGebruikersGegevens[1]
    elif input == "password":
        return lstGebruikersGegevens[2]
    else:
        return "Error"

