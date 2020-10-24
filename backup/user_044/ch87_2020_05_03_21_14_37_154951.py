with open('churras.txt', 'r') as arquivo:
	linhas=arquivo.readlines()
	valor=0
	for i in linhas:
		linha=i.split(" " or ",")
		valor+=linha[1]*linha[2]
			
		
	print(valor)