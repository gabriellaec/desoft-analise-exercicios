distancia = int(input("distancia desejada: "))
if distancia <= 200:
    X = (0.5 * distancia)
    x = float("{0:.2f}".format(X))
    a1 = int(x)
    a2 = int(x * 100)%100
    b = str(a2) 
    if len(b) < 2 :
        b.append("0")
    a = str(a1) + "." + b
    print (a)
if distancia > 200:
    Y = 0.45 * (distancia - 200) + 100
    y = float("{0:.2f}".format(Y))
    a1 = int(y)
    a2 = int(y * 100)%100 
    a = str(a1) + "." + str(a2)
    print (a)