with open('churras.txt', 'r') as arquivo:
	x=arquivo.readlines()
    linhas=x.strip()
	valor=0
	for i in linhas:
		linha=i.split(",")
		valor+=float(linha[1])*float(linha[2])
			
		
	print(valor)