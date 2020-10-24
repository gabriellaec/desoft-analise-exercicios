with open ('palavras.txt','r') as arquivo:
	conteudo = arquivo.readlines()
i = 0
for e in conteudo:
    palavras=e.split()
    for j in palavras:
        if j.lower() == 'a':
            i+=1
print(i) 