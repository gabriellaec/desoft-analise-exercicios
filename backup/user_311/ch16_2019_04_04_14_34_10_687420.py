def distancia_euclidiana(x1,y1,x2,y2):
    d1 = abs(x1 - y1) 
    d2 = abs(x2 - y2)
    return d1 and d2

a = 1
b = 2
c = 3
d = 4
print (distancia_euclidiana(a,b,c,d))