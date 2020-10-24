with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
	i=0
	conteudo=conteudo.lower()
	if 'banana' in conteudo:
		i+=1
	print(i)
        