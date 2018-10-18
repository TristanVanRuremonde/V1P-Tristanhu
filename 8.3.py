invoer = 0
def program(invoer):
    invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

    lijst = invoer.split('-')
    lijst = [int(i) for i in lijst]
    lijst.sort()
    maxx = max(lijst)
    minn = min(lijst)
    aantal = len(lijst)
    som = (sum(lijst))
    gem = som / aantal
    zin1 = 'gesorteerde lijst van ints: ' + str(lijst)
    zin2 = 'Grootste getal: ' + str(maxx) + ' en Kleinste getal: ' + str(minn)
    zin3 = 'Aantal getallen: ' + str(aantal) + 'som van getallen: ' + str(som)
    zin4 = 'gemmidelde: ' + str(gem)
    print(zin1)
    print(zin2)
    print(zin3)
    print(zin4)
program(invoer)