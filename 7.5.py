
def gemiddelde(woorden):
    acc = 0
    splits = woorden.split(" ")
    print(splits)
    for woord in splits:
        for letters in woord:
            acc += 1
    print(acc)
    gem = acc / len(splits)
    print(gem)
    return gem

gemiddelde('No cloud was brave enough to fill the void as was the tar on the Welken')
