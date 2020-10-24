d = int(input("Qual a distancia a ser percorrida em sua viagem? "))

if d <= 200:
    print("{0:.2f}".format(d * 0.5))
if d > 200:
    print("{0:.2f}".format(100 + ((d - 200) * 0.45)))