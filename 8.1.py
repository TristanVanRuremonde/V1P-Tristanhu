def seizoen(maand):
    if maand > 11 or maand < 3:
        print("Winter")
    elif maand > 2 and maand < 6:
        print("Lente")
    elif maand > 5 and maand < 9:
        print("Zomer")
    elif maand > 8 and maand < 12:
        print("Herfst")
    else:
        print("error")

seizoen(4)