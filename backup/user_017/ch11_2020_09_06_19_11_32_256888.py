def distancia_euclidiana(x1,x2,y1,y2):
    d= ((x2-x1)**2 + (y2-y1)**2)**0.5
    return d
w=5
x=1
y=4
z=1

a= distancia_euclidiana(w,x,y,z)

print(a)
    