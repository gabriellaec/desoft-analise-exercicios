with open ('macacos-me-mordam.txt','r') as arquivo:
	conteudo = arquivo.read().lower().split()
soma = 0 
for i in conteudo:
	if i == 'banana':
		soma += 1
print(soma)

