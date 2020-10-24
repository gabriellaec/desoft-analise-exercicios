d = int(input("Qual a distancia a ser percorrida em sua viagem? "))

if d <= 200:
    print("{0:.2f}".format(d * 0.5))
elif d > 200:
    print("{0:.2f}".format((200 * 0.5) + (d - 200 * 0.45)))