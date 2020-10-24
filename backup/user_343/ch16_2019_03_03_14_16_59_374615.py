def distancia_euclidiana(x1, y1, x2, y2):
    y = ((x2-x1)**2+(y2-y1)**2)**1/2
    return y
print (distancia_euclidiana(2, 4, 8, 12))