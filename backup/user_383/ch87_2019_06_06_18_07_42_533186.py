with open('churras.txt','r')as arquivo:
	conteudo = arquivo.readline()
	custo=[]
	valor=[]
	i = 0
	for linha in conteudo:
		churras=conteudo.split(',')
		custo.append(int(churras[1]))
		custo.append(float(churras[2]))
        while i < len(custo):
            valor.append(custo[i]*custo[i+1])
            i += 1
	total=sum(valor)
	print(total)

    