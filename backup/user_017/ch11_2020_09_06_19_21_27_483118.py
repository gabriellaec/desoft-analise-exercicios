def distancia_euclidiana(x2,x1,y2,y1):
    d= ((x2-x1)**2 + (y2-y1)**2)**0.5
    return d
r=5
s=1
t=4
u=1

a= distancia_euclidiana(r,s,t,u)

print(a)
    