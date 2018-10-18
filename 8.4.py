studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    lijst = []
    for student in studentencijfers:
        gem = sum(student) / len(student)
        lijst.append(gem)
    antw = lijst
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    lijst2 = []
    for student in studentencijfers:
        gem = sum(student) /len(student)
        lijst2.append(gem)

    antw = sum(lijst2) / len(lijst2)
    antw = int(antw)
    return antw


print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))