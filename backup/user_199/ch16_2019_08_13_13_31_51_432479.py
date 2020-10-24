def distancia_euclidiana(x1,y1,x2,y2):
    dxy=(((x2-x1)**2)+((y2-y1)**2))*0.5
    return dxy

x1=2
x2=4
y1=8
y2=2
print (distancia_euclidiana(x1,y1,x2,y2))