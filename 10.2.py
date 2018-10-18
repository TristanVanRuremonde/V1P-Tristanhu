import random

def monopolyworp():
    print('Worp speler')
    counter = 0
    while counter < 3:

        dobbel1 = random.randrange(1,7)
        dobbel2 = random.randrange(1,7)
        print(dobbel1, '+', dobbel2, '=', dobbel2 + dobbel1)

        if dobbel1 == dobbel2:
            counter += 1
            continue
        elif dobbel1 != dobbel2:
            break
    if counter > int(2):
        print('Je gaat naar de gevangenis, let op! laat de zeep niet vallen!')

    beurt()
def beurt():
    inputter = input('Volgende speler klaar? (Y/N): ')
    if inputter == 'Y' or 'y':
        monopolyworp()
    elif inputter != 'Y' or 'y':
        beurt()

beurt()
