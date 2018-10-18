def inlezen_beginstation(stations):
    while True:
        eerste_station = input("Beginstation: ")
        if eerste_station in stations:
            return eerste_station


def inlezen_eindstation(stations, beginstation):
    while True:
        laatste_station = input('Eindstation: ')
        if laatste_station in stations:
            if stations.index(laatste_station) > stations.index(beginstation):
                return laatste_station
        print("error")

def tussenstations():
    for tussenstations in range(stations.index(beginstation) +1, stations.index(eindstation)):
        print(stations[tussenstations], " ", end='')

def omroepen_reis(stations, beginstation, eindstation):

    print(stations.index(beginstation) + 1, beginstation)
    print(stations.index(eindstation) + 1, eindstation)
    afstand = (stations.index(eindstation)) - (stations.index(beginstation))
    print(afstand, 'Stations afgelegd')
    print("Ritprijs = ", afstand * 5)
    print("Beginstation: ", beginstation)
    print("Tussenstaions: ")
    print(tussenstations())
    print("Eindstation: ", eindstation)



stations = ['Schagen', 'Heerhugowaard',"Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk"
            , "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch"
            , "Eindhoven", "Weert", "Roermond", 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)