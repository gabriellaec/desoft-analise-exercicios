with open ('macacos-me-mordam.txt','r') as arquivo:
	conteudo = arquivo.readlines()
i = 0
for e in conteudo:
    palavras=e.split()
    for j in palavras:
        if j.lower() == 'banana':
            i+=1
print(i)