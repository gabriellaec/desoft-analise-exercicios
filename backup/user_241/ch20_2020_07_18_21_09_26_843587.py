distancia = int(input("distancia desejada: "))
if distancia <= 200:
    x = (0.5 * distancia)
    round(x,2)
    print (x)
if distancia > 200:
    y = ((0.45 * distancia) + 100)
    round(y,2)
    print (y)