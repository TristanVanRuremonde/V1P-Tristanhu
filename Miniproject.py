import random
import string
import csv


lstUniqueNumbers = []


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


def gebruikersInformatie():
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
    with open('Gebruikersbestand.csv', 'w', newline = '') as CSV:
        writer = csv.writer(CSV, delimiter=';')

        writer.writerow((gebruikersNummer, naamUser, wachtwoord))


gebruikersInformatie()
print(uniqueNumber())