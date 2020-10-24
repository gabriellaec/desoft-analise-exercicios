x1=int(input('x1?:'))
y1=int(input('y1?:'))
x2=int(input('x2?:'))
y2=int(input('y2?:'))
def distancia_euclidiana(x1,y1,x2,y2):
    dis = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dis)
