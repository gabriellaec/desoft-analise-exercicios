def distancia_euclidiana (x1, y1, x2, y2):
    d1 = (x2 - x1)**2
    d2 = (y2 - y1)**2
    resultado= (d1+d2)**(1/2)
    return resultado