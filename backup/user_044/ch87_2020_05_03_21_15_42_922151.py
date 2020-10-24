with open('churras.txt', 'r') as arquivo:
	linhas=arquivo.readlines()
	valor=0
	for i in linhas:
		linha=i.split(" " or ",")
		valor+=float(linha[1])*float(linha[2])
			
		
	print(valor)