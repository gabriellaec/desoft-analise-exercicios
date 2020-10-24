contador=0
with open('macacos-me-mordam.txt','r') as arquivo:
	conteudo = arquivo.read()
cont=conteudo.split()
for i in cont:
    e=i.lower()
    if e=="banana":
        contador+=1
print(contador)

            