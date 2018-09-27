kaartnummers = 'D:\Documenten\School\Huiswerk\PROG\kaartnummers.txt'
def opdracht(kaartnummers):
    openfile = open(kaartnummers, 'r')
    lijnteller = openfile.readlines()
    openfile.close()
    lengte = len(lijnteller)
    hoogste = 0;
    for regel in lijnteller:
        woorden = regel.split(', ')
        getal = int(woorden[0])
        if getal > hoogste:
            hoogste = getal

    print(hoogste)
    return lengte

openopdr = opdracht(kaartnummers)
zin1 = "Deze file kent " + str(openopdr) + " Regels"
print(zin1)
