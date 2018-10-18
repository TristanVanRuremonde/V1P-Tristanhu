import csv
lijstje = ['', '', 0]

with open('file.csv', 'r') as CSV:
    reader = csv.reader(CSV, delimiter=';')

    for row in reader:
        if int(row[2]) > int(lijstje[2]):
            lijstje = row

print(lijstje[0], 'had met ', lijstje[2], ' de hoogste score op ', lijstje[1])
