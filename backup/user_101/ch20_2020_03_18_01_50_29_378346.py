distancia=input("Qual a distancia, em km, que você deseja percorrer? ")
mais=0.45*distancia
menos=0.50*distancia
if distancia<=200:
	print (0.50*distancia)
else:
    print (0.50*distancia+0.45*(distancia-200))