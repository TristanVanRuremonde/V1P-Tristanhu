#Geef een string van vier letters: worst
#worst heeft 5 letters
#Geef een string van vier letters: oliebol
#oliebol heeft 7 letters
#Geef een string van vier letters: drop
#Inlezen van correcte string: drop is geslaagd


def letters():
    while True:
        woord = input('geef woord: ')
        letters = len(woord)
        zin1 = str(woord) + ' heeft ' + str(letters) + ' letters'
        zin2 = 'Inlezen van correcte sting: ' + str(woord) + ' is geslaagd'
        if letters != 4:
            print(zin1)
        else:
            print(zin2)
            break
letters()