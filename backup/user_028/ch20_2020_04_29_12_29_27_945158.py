distancia=int(input('Qnts km?'))
d=distancia-200
if distancia <= 200:
    preco = distancia* 0.5
    print(preco,'{:.2f}'.format(preco))
else:
    x=(distancia-200) * 0.05
    preco = distancia * 0.5 - x
    print(preco,'{:.2f}'.format(preco))
       