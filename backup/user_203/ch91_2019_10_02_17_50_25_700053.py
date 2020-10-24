with open('palavras.txt','r') as lista:
	conteudo = lista.read()
	lista = []
	i = 0
	while i<len(lista):
		if lista[i] == 'a' or lista[i] == 'A':
			i = i +1
	print(conteudo) 