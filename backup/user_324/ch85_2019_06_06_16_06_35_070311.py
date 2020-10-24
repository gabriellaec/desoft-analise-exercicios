contador=0
with open('macacos-me-mordam.txt','r') as arquivo:
	conteudo = arquivo.read()
cont=conteudo.split()
for i in cont:
    if i=="banana":
        contador+=1
print(contador)

            