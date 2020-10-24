distancia=int(input('Qnts km?'))
i=0
while i <= 200:
    preco= 0.5*distancia
    i+=1
    if i > 200:
        preco2= preco + (0.45*(distancia-200))
print(preco2)
       