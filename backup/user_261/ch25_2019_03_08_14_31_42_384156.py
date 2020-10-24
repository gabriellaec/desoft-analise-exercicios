a= float(input("distância qu você deseja percorrer:"))
if a<=200:
	y= 0.50*a	
else:
	y= 100 + (a-200)*0.45
print("preço da passagem é de {0:.2f}".format(y))
      
