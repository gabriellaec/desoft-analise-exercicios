distancia=float(input("qual distancia vc deseja percorrer em km?: "))
if distancia<=200:
    preco=distancia*0.50
else:
    preco=200*0.50+(distancia-200)*0.45
print('{0:.2f}'.format(preco))