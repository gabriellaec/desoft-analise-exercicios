with open('churras.txt','r')as arquivo:
	conteudo = arquivo.readline()
	churras=conteudo.split(',')
	custo=[]
	valor=[]
	for linha in churras:
		custo.append(int(churras[1]))
		custo.append(float(churras[2]))
	for i in custo:
		valor = custo[i]*custo[i+1]
	total=sum(valor)
	print(total)

    