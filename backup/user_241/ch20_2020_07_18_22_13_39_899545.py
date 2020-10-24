distancia = int(input("distancia desejada: "))
if distancia <= 200:
    X = (0.5 * distancia)
    x = float("{0:.2f}".format(X))
    a1 = int(x)
    a2 = int(x * 100)%100 
    print (a1 ,".", a2)
if distancia > 200:
    Y = 0.45 * (distancia - 200) + 100
    y = float("{0:.2f}".format(Y))
    a1 = int(y)
    a2 = int(y * 100)%100 
    print (a1 ,".", a2)