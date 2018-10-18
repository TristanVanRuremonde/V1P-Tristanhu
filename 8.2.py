lijstje = 0
def program(lijstje):
    lijstje = eval(input("Geef lijst met minimaal 10 strings: "))
    apartelijst = []
    for woorden in lijstje:
        if len(woorden) == 4:
            apartelijst.append(woorden)
    print(apartelijst)

program(lijstje)