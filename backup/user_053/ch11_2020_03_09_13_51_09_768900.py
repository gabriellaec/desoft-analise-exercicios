def distancia_euclidiana(x1,y1,x2,y2):
    distancia=(((x2-x1)**2)+((y2-y1)**2))**0.5
    return distancia

a=3
c=4
d=5
e=6
b=distancia_euclidiana(a,c,d,e)

print(b)