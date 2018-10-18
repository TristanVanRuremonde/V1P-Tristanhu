

def menu():
    print("=================================================\
    \n1: Ik wil weten hoeveel kluizen er nog vrij zijn\
    \n2: Ik wil een nieuwe kluis\
    \n3: Ik wil even mijn kluis openen\
    \n4: Ik geef mijn kluis terug\
    \n5: Ik wil stoppen\
    \n=================================================")

    keuze = int(input("Welke optie kiest u? \n"))

    if keuze == 1:
        toon_aantal_kluizen_vrij()
    elif keuze == 2:
        nieuwe_kluis()
    elif keuze == 3:
        kluis_openen()
    elif keuze == 4:
        kluis_teruggeven()
    elif keuze == 5:
        raise SystemExit(0)


def toon_aantal_kluizen_vrij():
    aantal_bezet = 0
    bestand_read = open("kluizen.txt", "r+")

    for regel in bestand_read.readlines():
        aantal_bezet += 1

    print("Er zijn", 12 - aantal_bezet, "lege kluizen.\n")
    bestand_read.close()


def nieuwe_kluis():
    aantal_bezet = 0
    bestand_read = open("kluizen.txt", "r+")

    for regel in bestand_read.readlines():
        aantal_bezet += 1

    bestand_read.close()

    if aantal_bezet < 12:
        standaard_lijst = list(range(1, 13))
        bestand_read = open("kluizen.txt", "r+")

        for item in bestand_read:
            kluisnummer = int(item[0])
            if kluisnummer in standaard_lijst:
                standaard_lijst.remove(kluisnummer)

        bestand_read.close()

        ww_ingevuld = input("Wat wilt u als wachtwoord instellen? \n")

        bestand_append = open("kluizen.txt", "a")
        bestand_append.write(str(min(standaard_lijst)) + ";" + str(ww_ingevuld) + "\n")
        print("U krijgt kluis", min(standaard_lijst), "met code", ww_ingevuld, "\n")

    else:
        print("Geen vrije kluizen meer.\nOnze excuses.")

    bestand_append.close()


def kluis_openen():
    bestand_read = open("kluizen.txt", "r+")
    regel = bestand_read.readlines()
    bestand_read.close()

    kluisnummer_ingevuld = input("Welke kluis is van u: ")
    ww_ingevuld = input("Wat is uw wachtwoord: ")

    i = False
    for x in regel:
        regel_split = x.split(";")
        kluisnummer_bestand = regel_split[0]
        ww_bestand = regel_split[1].strip()

        if kluisnummer_ingevuld == kluisnummer_bestand and ww_ingevuld == ww_bestand:
            i = True
    if i:
        print("Uw kluis is open")
    else:
        print("U heeft iets verkeerd ingevuld")


def kluis_teruggeven():
    bestand_read = open("kluizen.txt", "r+")
    regel = bestand_read.readlines()
    bestand_read.close()

    kluisnummer_ingevuld = input("Welke kluis is van u: ")
    ww_ingevuld = input("Wat is uw wachtwoord: ")

    bestand_write = open("kluizen.txt", "w")

    for x in regel:
        regel_split = x.split(";")
        kluisnummer_regel = regel_split[0]
        ww_regel = regel_split[1].strip()

        if kluisnummer_ingevuld != kluisnummer_regel and ww_ingevuld != ww_regel:
            bestand_write.write(str(kluisnummer_regel) + ";" + str(ww_regel) + "\n")
    bestand_write.close()


while True:
menu()

counter = 0
lijst = []
with open('file.csv', newline='') as CSV:
    for i in CSV.readlines():

        split1 = i.split(';')[0]
        split2 = i.split(';')[1]
        split3 = i.split(';')[2].strip('\n')
        split3 = split3.strip('\r')
        lijst.append(split3)


        if int(split3) > int(counter):
            counter = split3
        print(CSV.readlines().index(max(lijst)))
#lijst = [int(a) for a in lijst]
print(counter)
print(lijst)
print(max(lijst))


int(input("Wat wil je doen?: \n 1.Inloggen \n 2. Registratie"))
