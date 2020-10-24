distancia=int(input("qual distancia vc deseja percorrer em km?: "))
if distancia<=200:
    preco=distancia*0.50
    print(round(preco,2))
else:
    preco=200*0.50+(distancia-200)*0.45
    print(round(preco,2))