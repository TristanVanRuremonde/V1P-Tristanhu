filename = 0
dictionary = {}
dictionary2 = {}
def ticket(filename):

    filename = open('D:/Documenten/School/Huiswerk/PROG/ticker.txt', 'r+')
    for line in filename:
        splitter = line.split(':')
        value = splitter[0]
        keys = splitter[1]

        dictionary[value] = keys.strip()
        dictionary2.update([(v,k) for k,v in dictionary.items()])
        #dictionary.update([(v,k) for k,v in dictionary.items()])
        #for items in splitter:
        #    dictionary[keys, values] = [keys, values in splitter]

    return dictionary, dictionary2

def checker():
    woordtocheck = input('Enter company name: ')
    output = dictionary.get(woordtocheck)
    print(output)
    ticktocheck = input('Enter ticker symbol: ')
    output2 = dictionary2.get(ticktocheck)

    return output2




print(ticket(filename))
print(checker())