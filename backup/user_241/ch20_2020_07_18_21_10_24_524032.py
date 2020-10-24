distancia = int(input("distancia desejada: "))
if distancia <= 200:
    X = (0.5 * distancia)
    x = round(X,2)
    print (x)
if distancia > 200:
    Y = ((0.45 * distancia) + 100)
    y = round(Y,2)
    print (y)