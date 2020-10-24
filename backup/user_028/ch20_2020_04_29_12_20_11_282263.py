distancia=int(input('Qnts km?'))
i=0
d=distancia-200
while i <= 200:
    preco= 0.5*distancia
    i+=1
    if i > 200:
        preco2= preco + (0.45*d)
print(preco2)
       