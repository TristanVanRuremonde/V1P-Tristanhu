def som():
    totaal = 0
    aantal = 0
    while True:
        plus = int(input('Geef getal: '))
        if plus == 0:
            break
        aantal += 1
        totaal = totaal + plus
    zin1 = 'Er zijn ' + str(aantal) + ' getallen ingevoerd, de som is: ' + str(totaal)
    print(zin1)

som()