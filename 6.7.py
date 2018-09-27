def standaardprijs(afstandKM):

    kosten = 0.80 * afstandKM
    if afstandKM > 50:
        kosten = 15 + (0.16 * afstandKM)
    if afstandKM < 0:
        kosten = 0
    print(kosten)


def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardprijs(afstandKM) = afstandKM
    if leeftijd < 12 or leeftijd > 64:
        kosten = ((0.80 /100) *30) * afstandKM
    if weekendrit == True and (leeftijd < 12 or leeftijd > 64):
        kosten = ((0.80 /100) * 35) * afstandKM
    if weekendrit == True and (leeftijd > 12 or leeftijd < 64):
        kosten = ((0.80 /100) * 40) * afstandKM
    else:
        kosten = 0.80 * afstandKM
    print(kosten)



print(ritprijs(12, True, 60))
print(standaardprijs(70))
