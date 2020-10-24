def distancia_euclidiana(x1,y1,x2,y2):
    return ((((x1-x2)**2)+((y1-y2)**2))**(1/2))
    
x1=float(input('X do primeiro ponto: '))
y1=float(input('Y do primeiro ponto: '))
x2=float(input('X do segundo ponto: '))
y2=float(input('Y do segundo ponto: '))

print(distancia_euclidiana(x1,y1,x2,y2))