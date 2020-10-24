def distancia_euclidiana (x1,x2,y1,y2):
    distancia = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)
    return distancia

print(distancia_euclidiana(x1,x2,y1,y2))