
def code(invoerstring):
    for teken in invoerstring:
        rangnummer = ord(teken)
        rangnummer3 = int(rangnummer) + 3
        print(chr(rangnummer3), end='')

code("iets, iets, zwartepieten discussie")

