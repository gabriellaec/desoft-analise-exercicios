x1 = 2
y1 = 4
x2 = 3
y2 = 6

def distancia_euclidiana(x1,y1,x2,y2):
    d = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    return d

print(distancia_euclidiana(x1,y1,x2,y2))