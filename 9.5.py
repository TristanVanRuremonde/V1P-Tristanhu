dictionary = {}
def namen():
    while True:
        naam = input('Noem naam: ')
        if naam in dictionary:
            dictionary[naam] += 1
        elif naam == '':
            break
        else:
            dictionary[naam] = 1

    for k,v in dictionary.items():
        if v < 2:
            print('er is {} student met de naam {}'.format(v,k))
        else:
            print('er zijn {} studenten met de naam {}'.format(v,k))



namen()