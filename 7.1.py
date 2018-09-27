def convert(Celsius):
    fahrenheit = Celsius * 1.8 + int(32)
    return fahrenheit
print(convert(25))

celsius = 0
for i in range(-30, 41, 10):
    celsius = i * 1.8 + 32
    print ('{:4} {:5}'.format(i, celsius))