def distancia_euclidiana(x1,y1,x2,y2):
    z = (x2-x1)**2+((y2-y1)**2)**0.5
    return z
print (distancia_euclidiana(2,4,6,8))