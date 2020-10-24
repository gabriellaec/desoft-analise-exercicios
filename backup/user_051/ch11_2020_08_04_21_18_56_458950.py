def distancia_euclidiana(X1, y1, X2, y2):
    return ((X2-X1)**2+(y2-y1)**2)**1/2
print (distancia_euclidiana(10, 10, 14, 14))