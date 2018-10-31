from tkinter import *
from tkinter.messagebox import showinfo
import methodsFile
import captchaprogram
import datetime
from PIL import Image, ImageTk
huidigeTijd = (str(datetime.datetime.now()).split(' ')[1]).split(':')[0], ':', (str(datetime.datetime.now()).split(' ')[1]).split(':')[1]
unicode = ''
naamUser = ''
maxStallingen = 50
counter = 0
generatedcaptcha = captchaprogram.createCaptcha()
x = 0


def randomize():
    'Zorgt voor een random plaatje als captcha'
    global generatedcaptcha
    captchaPlaatje.destroy()
    generatedcaptcha = captchaprogram.createCaptcha()
    img = ImageTk.PhotoImage(Image.open("pil_text_font.png"))
    nieuwPlaatje = Label(master=captchaframe, image=img)
    nieuwPlaatje.image = img
    nieuwPlaatje.grid(row=1, column=1)


def aantalStallingen():
    'Laat de gebruiker het aantal vrije stallingen zien'
    gebruikteStallingen = 0
    with open('Gebruikersbestand.csv', 'r') as CSV:
        for _ in CSV.readlines():
            gebruikteStallingen += 1
    beschikbareStallingen = maxStallingen - gebruikteStallingen
    return beschikbareStallingen


def login():
    'Laat de gebruiker inloggen'
    username = usernamefield.get()
    password = passwordfield.get()
    global unicode
    unicode = username
    ingelogd = methodsFile.logineenmalig(username, password)
    if ingelogd == False:
        showinfo(title="Error", message="Onjuiste gegevens. Probeer het nog eens")
    else:
        tooncaptchaframe()


def register():
    'Laat de gebruiker registreren'
    if aantalStallingen() == 0:
        showinfo(title="Error", message="Alle stallingen zijn al in gebruik")
    else:
        voornaam = voornaamfield.get()
        tussenvoegsel = tussenvoegselfield.get()
        achternaam = achternaamfield.get()
        wachtwoord = wachtwoordfield.get()
        uniekeCode = methodsFile.registreren(voornaam, tussenvoegsel, achternaam, wachtwoord)
        if uniekeCode == "" and (voornaam == "" or achternaam == ""):
            showinfo(title="Error", message="Naam onvolledig")
        elif uniekeCode == "":
            showinfo(title="Error",
                     message="Vul een geldig wachtwoord in (langer dan 6 karakters met 2 of meer getallen")
        else:
            uniekeCode = ('Unieke code: ' + uniekeCode)
            showinfo(title="Geregistreerd", message=uniekeCode)
            toonloginframe()


def correcteCaptcha():
    'Checkt of de captcha correct is en handelt het af'
    global x, counter
    captchavalue = captchaInput.get()
    if captchavalue == generatedcaptcha:
        tooningelogdframe()
        counter = 0
    elif counter == 2:
        showinfo(title="Error", message="3 slag = uit.")
        toonloginframe()
        counter = 0
    else:
        counter += 1
        pogingenover = 3-counter
        showinfo(title="Error", message="Probeer het nog eens. Je hebt nog " + str(pogingenover) + " pogingen over.")



def openStalling():
    'Laat de gebruiker weten dat de stalling geopend is'
    positief = methodsFile.openStalling(unicode)
    if positief == True:
        showinfo(title="Open", message="Fiets kan worden gestald.")
    else:
        showinfo(title="Error", message="Iets ging fout")


def fietsOphalen():
    'Laat de gebruiker weten dat de fiets kan worden gestald'
    positief = methodsFile.fietsOphalen(unicode)
    if positief == True:
        showinfo(title="Open", message="Fiets kan worden opgehaald.")
    else:
        showinfo(title="Error", message="Iets ging fout")


def persoonlijkeinfo():
    'Laat de gebruiker persoonlijke informatie zien - de tijd die de fiets het meest recent in de stalling stond'
    tijdinstalling = methodsFile.persoonlijkeInformatie(unicode)
    if tijdinstalling == "Een van de tijden (of beiden) is/zijn leeg" or tijdinstalling == "Error 40404040":
        showinfo(title="Error", message="Iets ging fout")
    else:
        showinfo(title="Persoonlijke informatie", message="Tijd in stalling gespendeerd: " + str(tijdinstalling))


def tooncaptchaframe():
    'Toont de captchaframe in de GUI'
    randomize()
    captchaInput.delete(0, END)
    loginframe.grid_forget()
    captchaframe.grid()


def toonregisterframe():
    'Toont de registerframe in de GUI    '
    huidigeTijd = (str(datetime.datetime.now()).split(' ')[1]).split(':')[0], ':', \
                  (str(datetime.datetime.now()).split(' ')[1]).split(':')[1]
    global tijdLabel
    tijdLabel["text"] = huidigeTijd
    tijdframe.grid_forget()
    tijdframe.grid()
    loginframe.grid_forget()
    registerframe.grid()
    voornaamfield.delete(0, END)
    tussenvoegselfield.delete(0, END)
    achternaamfield.delete(0, END)
    wachtwoordfield.delete(0, END)


def toonloginframe():
    'Toont het loginframe in de GUI'
    huidigeTijd = (str(datetime.datetime.now()).split(' ')[1]).split(':')[0], ':', \
                  (str(datetime.datetime.now()).split(' ')[1]).split(':')[1]
    global tijdLabel
    tijdLabel["text"] = huidigeTijd
    tijdframe.grid_forget()
    captchaframe.grid_forget()
    tijdframe.grid()
    registerframe.grid_forget()
    loginframe.grid()
    labelAantalStallingen = Label(master=loginframe, text=("Aantal vrije stallingen: " + str(aantalStallingen())))
    labelAantalStallingen.grid(row=5, column=1)
    usernamefield.delete(0, END)
    passwordfield.delete(0, END)


def tooningelogdframe():
    'Toont het ingelogdframe in de GUI'
    with open('Gebruikersbestand.csv', 'r') as CSV:
        for o in CSV.readlines():
            if unicode == o.split(';')[0]:
                global naamUser
                naamUser = o.split(';')[1]
                break
        CSV.close()
    captchaframe.grid_forget()
    labelBericht = Label(master=ingelogdframe, text=('Welkom, ' + naamUser))
    labelBericht.grid(row=0, column=3)
    labelAantalStallingen = Label(master=ingelogdframe, text=("Aantal vrije stallingen: " + str(aantalStallingen())))
    labelAantalStallingen.grid(row=5, column=2)
    ingelogdframe.grid()


def logout():
    'Logt uit en brengt gebruiker terug naar loginframe'
    randomize()
    huidigeTijd = (str(datetime.datetime.now()).split(' ')[1]).split(':')[0], ':', \
                  (str(datetime.datetime.now()).split(' ')[1]).split(':')[1]
    global tijdLabel
    tijdLabel["text"] = huidigeTijd
    tijdframe.grid_forget()
    tijdframe.grid()
    loginframe.grid_forget()
    ingelogdframe.grid_forget()
    loginframe.grid()
    usernamefield.delete(0, END)
    passwordfield.delete(0, END)


root = Tk()
root.geometry("450x200")
tijdframe = Frame(master=root)
tijdframe.grid()
tijdLabel = Label(master=tijdframe, text=huidigeTijd)
tijdLabel.grid(row=0, column=3)

#captchaframe zooi
captchaframe = Frame(master=root)

captchaText = Label(master=captchaframe, text='Vul de CAPTCHA in:')
captchaText.grid(row=0, column=1)

img = ImageTk.PhotoImage(Image.open("pil_text_font.png"))
captchaPlaatje = Label(master=captchaframe, image=img)
captchaPlaatje.grid(row=1, column=1)

captchaInput = Entry(master=captchaframe)
captchaInput.grid(row=2, column=1, sticky="EW")
inputButton = Button(master=captchaframe, text="OK", command=correcteCaptcha)
inputButton.grid(row=2, column=2, sticky="EW")
inputButton = Button(master=captchaframe, text="try again", command=randomize)
inputButton.grid(row=2, column=3, sticky="EW")

# loginframe zooi
loginframe = Frame(master=root)
loginframe.grid()
labelUsername = Label(loginframe, text="Gebruikersnaam: ")
labelUsername.grid(row=1, column=1, sticky="EW")
labelPassword = Label(loginframe, text="Wachtwoord: ")
labelPassword.grid(row=2, column=1, sticky="EW")
usernamefield = Entry(loginframe)
usernamefield.grid(row=1, column=2, sticky="EW")
passwordfield = Entry(loginframe)
passwordfield.grid(row=2, column=2, sticky="EW")
buttonLogin = Button(loginframe, text="Inloggen", command=login)
buttonLogin.grid(row=3, column=2, sticky="EW")
buttonRegister = Button(loginframe, text="Registreren", command=toonregisterframe)
buttonRegister.grid(row=3, column=0, sticky="EW")
labelAantalStallingen = Label(master=loginframe, text=("Aantal vrije stallingen: " + str(aantalStallingen())))
labelAantalStallingen.grid(row=5, column=1)

# registerframe zooi
registerframe = Frame(master=root)
labelVoornaam = Label(registerframe, text="Voornaam: ")
labelVoornaam.grid(row=1, column=0, sticky="EW")
labelTussenvoegsel = Label(registerframe, text="Tussenvoegsel: ")
labelTussenvoegsel.grid(row=2, column=0, sticky="EW")
labelAchternaam = Label(registerframe, text="Achternaam: ")
labelAchternaam.grid(row=3, column=0, sticky="EW")
labelWachtwoord = Label(registerframe, text="Wachtwoord: ")
labelWachtwoord.grid(row=4, column=0, sticky="EW")
voornaamfield = Entry(registerframe)
voornaamfield.grid(row=1, column=1, sticky="EW")
tussenvoegselfield = Entry(registerframe)
tussenvoegselfield.grid(row=2, column=1, sticky="EW")
achternaamfield = Entry(registerframe)
achternaamfield.grid(row=3, column=1, sticky="EW")
wachtwoordfield = Entry(registerframe)
wachtwoordfield.grid(row=4, column=1, sticky="EW")
buttonRegistreren = Button(registerframe, text="Registreren", command=register)
buttonRegistreren.grid(row=5, column=0, sticky="EW")
buttonTerug = Button(registerframe, text="Terug", command=toonloginframe)
buttonTerug.grid(row=5, column=1, sticky="EW")

# ingelogd frame
ingelogdframe = Frame(master=root)
buttonUitloggen = Button(master=ingelogdframe, text="Uitloggen", command=logout)
buttonUitloggen.grid(row=3, column=3, sticky="EW")
buttonOpenStalling = Button(master=ingelogdframe, text="Open stalling", command=openStalling)
buttonOpenStalling.grid(row=2, column=2, sticky="EW")
buttonFietsOphalen = Button(master=ingelogdframe, text="Fiets ophalen", command=fietsOphalen)
buttonFietsOphalen.grid(row=2, column=3, sticky="EW")
buttonPersoonlijkeInfo = Button(master=ingelogdframe, text="Persoonlijke informatie", command=persoonlijkeinfo)
buttonPersoonlijkeInfo.grid(row=2, column=4, sticky="EW")



root.mainloop()
