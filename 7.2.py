kaartnummers = open('D:\Documenten\School\Huiswerk\PROG\kaartnummers.txt', 'r')
def opdracht(kaartnummers):
    for line in kaartnummers:
        print(line, end='')

        print("yooo")
    kaartnummers.close()
    return
print(opdracht(kaartnummers))