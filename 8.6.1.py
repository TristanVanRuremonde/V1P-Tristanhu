file = open('D:/Documenten/School/Huiswerk/PROG/kluizen.txt', 'r+')
antw = 0


def toon_aantal_kluizen_vrij():
    counter = 0
    file = open('D:/Documenten/School/Huiswerk/PROG/kluizen.txt', 'r')
    for lines in file:
        counter += 1
    print(12 - int(counter))


def nieuwe_kluis():
    counter = 0
    bestand_read = open('D:/Documenten/School/Huiswerk/PROG/kluizen.txt', "r+")

    for regel in bestand_read.readlines():
        counter += 1

    bestand_read.close()

    if counter < 12:
        standaard_lijst = list(range(1, 13))
        bestand_read = open('D:/Documenten/School/Huiswerk/PROG/kluizen.txt', "r+")

        for item in bestand_read:
            kluisnummer = int(item[0])
            if kluisnummer in standaard_lijst:
                standaard_lijst.remove(kluisnummer)

        bestand_read.close()

        ww_ingevuld = input("Wat wilt u als wachtwoord instellen? \n")

        bestand_append = open('D:/Documenten/School/Huiswerk/PROG/kluizen.txt', "a")
        bestand_append.write(str(min(standaard_lijst)) + ";" + str(ww_ingevuld) + "\n")
        print("Kluis nummer ", min(standaard_lijst), " is aangewezen, met code", ww_ingevuld, "\n")
        bestand_append.close()

    else:
        print("Geen vrije kluizen meer.\nOnze excuses.")





def kluis_openen():
    bestand_read = open('D:/Documenten/School/Huiswerk/PROG/kluizen.txt', "r+")
    regel = bestand_read.readlines()
    bestand_read.close()

    kluisnummer_ingevuld = input("Welke kluis is van u: ")
    ww_ingevuld = input("Wat is uw wachtwoord: ")

    kluisopenen = False
    for x in regel:
        regel_split = x.split(";")
        kluisnummer_bestand = regel_split[0]
        ww_bestand = regel_split[1].strip()

        if kluisnummer_ingevuld == kluisnummer_bestand and ww_ingevuld == ww_bestand:

            kluisopenen = True
    if kluisopenen:
        print("De kluis is geopend")
    else:
        print("Error")

def kluis_teruggeven():
    bestand_read = open('D:/Documenten/School/Huiswerk/PROG/kluizen.txt', "r+")
    regel = bestand_read.readlines()
    bestand_read.close()

    kluisnummer_ingevuld = input("Welke kluis is van u: ")
    ww_ingevuld = input("Wat is uw wachtwoord: ")

    bestand_write = open('D:/Documenten/School/Huiswerk/PROG/kluizen.txt', "w")

    kluisteruggegeven = 0
    for x in regel:
        regel_split = x.split(";")
        kluisnummer_regel = regel_split[0]
        ww_regel = regel_split[1].strip()

        if kluisnummer_ingevuld != kluisnummer_regel and ww_ingevuld != ww_regel:
            bestand_write.write(str(kluisnummer_regel) + ";" + str(ww_regel) + "\n")
            kluisteruggegeven = True
        else:
            kluisteruggegeven = False
    if kluisteruggegeven:
        print("Kluis ingeleverd")
    bestand_write.close()





def keuzemenu(antw):
    antw = input('1: Ik wil weten hoeveel kluizen nog vrij zijn\n'
                 '2: Ik wil een nieuwe kluis\n3: Ik wil mijn kluis openen\n'
                 '4: Ik geef mijn kluis terug\n'': ')
    if antw == '1':
        toon_aantal_kluizen_vrij()

    elif antw == '2':
        nieuwe_kluis()

    elif antw == '3':
        kluis_openen()

    elif antw == '4':
        kluis_teruggeven()

    else:
        print('Error')

keuzemenu(antw)
