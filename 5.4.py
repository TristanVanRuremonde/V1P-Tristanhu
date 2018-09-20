lijst = "Maandag", "Dinsdag", "Woensdag"

for char in lijst:
    print(char[0]+char[1])


for woord in lijst:
    for counter in range(0, 2):
        print(woord[counter])


