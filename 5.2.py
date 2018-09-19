leeftijd = input("Wat is je leeftijd?: ")
paspoort = input("Heb je een nederlands paspoort, Y of N?: ")
print(leeftijd, paspoort)
if int(leeftijd) >= 18 and paspoort == "Y":
    print("je mag stemmen")
else:
    print("Sorry, je mag niet stemmen")