def lang_genoeg(lengte):
    lengte = input("Wat is je lengte?: ")
    if int(lengte) >= 120:
        return "Je bent lang genoeg voor de attractie"
    else:
        return "Sorry, je bent te klein"
print(lang_genoeg(0))