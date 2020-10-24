with open ("macacos-me-mordam.txt", 'r') as arquivo:
    conteudo= arquivo.read()
    contudo= conteudo.lower()
    ola=conteudo.split()
    a=0
    i=0
    cont=0
    lista=[]
for d in ola:
	if d == banana:
		i+=1
print(i)