def distancia_euclidiana(x1, y1, x2, y2):
    y = ((x2-x1)+(y2-y1))**1/2
    return y
print (distancia_euclidiana(2, 3, 5, 10))