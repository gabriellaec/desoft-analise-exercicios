a= float(input("distância qu você deseja percorrer:"))
if a<=200:
	y= 0.50*a
	print ("preço da passagem é de {0:.2f}.format{y}")
else:
	b= 100 + (200-y)*0.45
	print("preço da passagem é de {0:.2f}.format{b}")
      
