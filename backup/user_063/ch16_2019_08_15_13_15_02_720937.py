def distancia_euclidiana(x1,x2,y1,y2):
    D = ((x2-x2)**2+(y2-y1)**2)**(1/2)
    return D
a = distancia_euclidiana(1,4,3,7)
print (a)