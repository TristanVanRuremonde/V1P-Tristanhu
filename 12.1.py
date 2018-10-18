import xmltodict

def processXML(filename):
    with open(filename) as XML:
        filecontentstring = XML.read()
        xmldict =xmltodict.parse(filecontentstring)
        return xmldict

productdict = processXML('productxml.xml')
artikelnamen = productdict['artikelen']['artikel']

for artikelen in artikelnamen:
    print(artikelen['naam'])
