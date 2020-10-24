x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

def distancia_euclidiana (x1,x2,y1,y2):
    distancia = (((x1 - x2)**2) + ((y1 + y2)**2))**(1/2)
    return distancia