def bedrag():
    try:
        aantal = int(input("hoeveel mensen op reis?: "))
        persoonlijkbedrag = 4356 / aantal

        return persoonlijkbedrag
    except ZeroDivisionError:
        print('kan niet delen door nul')
    except ValueError:
        print('ja getal invullen kut')


    except IndexError:
        print('geen mingetal pls')
    except:
        print("errortje")


print(bedrag())