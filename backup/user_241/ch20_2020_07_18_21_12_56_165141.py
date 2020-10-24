distancia = int(input("distancia desejada: "))
if distancia <= 200:
    X = (0.5 * distancia)
    x = float("{0:.2f}".format(X))
    print (x)
if distancia > 200:
    Y = 0.45 * (distancia - 200) + 100
    y = float("{0:.2f}".format(Y))
    print (y)