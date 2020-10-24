distancia=float(input('quantos km vc deseja percorrer?'))
if distancia<=200:
    preco=distancia*0.5
    print ('{0:.2f}'.format(preco))
elif distancia>200:
    preco=200*0.5+(distancia-200)*0.45
    print ('{0:.2f}'.format(preco))