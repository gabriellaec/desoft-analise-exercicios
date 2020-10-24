def distancia_euclidiana(x1, y1, x2, y2):
    distancia = y2 - y1 / x2 - x1
    print("A distancia entre os pontos é: {0}".format(distancia))
x1 = float(input("Entre com x1: "))
x2 = float(input("Entre com x2: "))
y1 = float(input("Entre com y1: "))
y2 = float(input("Entre com y2: "))
distancia_euclidiana(x1, y1, x2, y2)
