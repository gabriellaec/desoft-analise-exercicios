with open ("macacos-me-mordam.txt","r") as arquivo:
    conteudo=arquivo.read()
conteudo.lower()
c = 0
for palavra in conteudo:
	if palavra == "banana":
        c+=1
print(c)
