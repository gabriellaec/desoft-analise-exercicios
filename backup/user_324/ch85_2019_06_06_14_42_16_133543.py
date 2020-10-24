contador=0
with open('macacos-me-mordam.txt','r') as arquivo:
	conteudo = arquivo.read()
for i in conteudo:
    if i=="banana":
        contador+=1
            