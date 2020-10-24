def distancia_euclidiana(x1, y1, x2, y2):
    d=((x2-x1)**2+(y2-y1)**2)**(1/2)
    return d

x1 = 1
y1 = 2
x2 = 3
y2 = 4

print(distancia_euclidiana(x1, y1, x2, y2))
