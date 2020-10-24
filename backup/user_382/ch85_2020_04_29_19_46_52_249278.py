with open ('macacos-me-mordam.txt','r') as arquivo:
	conteudo = arquivo.read().lower()
soma = 0 
conteudo = conteudo.split()
for i in conteudo:
	if i == 'banana':
		soma += 1
print(soma)

