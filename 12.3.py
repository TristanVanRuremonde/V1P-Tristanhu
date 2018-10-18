import xmltodict

def processXML(filename):
    with open(filename) as XML:
        filecontentstring = XML.read()
        xmldict =xmltodict.parse(filecontentstring)
        return xmldict

productdict = processXML('stations.xml')
stations = productdict['Stations']['Station']

for station in stations:
    print(station['Code'], '-' , station['Type'])

for station in stations:
    if station['Synoniemen'] is not None:
        print('Stations met synoniemen: ','\n', station['Synoniemen'])
for station in stations:
    print(station['Code'], '-', station['Namen']['Lang'])

