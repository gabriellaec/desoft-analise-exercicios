def distancia_euclidiana(x1,y1,x2,y2):
    distancia_dois_pontos = (((x2-x1)**2) + ((y2-y1)**2))**0.5
    return distancia_dois_pontos
a=1
b=3
c=2
d=5
e= distancia_euclidiana(a,b,c,d)
print(e)
