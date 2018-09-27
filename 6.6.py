lijst = ['a', 'b', 'c']
print(lijst)

def wijzig(letterlijst):
    letterlijst = lijst
    while len(lijst) > 0:
        lijst.pop()

    lijst.append('d')
    lijst.append('e')
    lijst.append('f')
    return letterlijst

print(wijzig(0))