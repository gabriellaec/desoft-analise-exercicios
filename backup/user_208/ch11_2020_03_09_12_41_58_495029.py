def distancia_euclidiana (x1,x2,y1,y2):
    dist_entre_dois_pontos= ((x1-x2)**2+(y1-y2)**2)**(1/2)
    return dist_entre_dois_pontos
x1=3
x2=4
y1=3
y2=5   
dist_entre_dois_pontos=distancia_euclidiana(x1,x2,y1,y2)
print (dist_entre_dois_pontos)