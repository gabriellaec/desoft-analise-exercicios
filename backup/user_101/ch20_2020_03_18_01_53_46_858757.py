distancia=float(input("Qual a distancia, em km, que você deseja percorrer? "))
mais=0.50*distancia+0.45*(distancia-200)
menos=0.50*distancia
if distancia<=200:
	print ("R${0:.2f}".format(menos))
else:
    print ("R${0:.2f}".format(mais))