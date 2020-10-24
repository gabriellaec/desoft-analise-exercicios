def distancia_euclidiana(x1, x2, y1, y2):
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    return d

print(distancia_euclidiana(5, 10, 10, 5))