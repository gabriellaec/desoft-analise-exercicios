with open ("macacos-me-mordam.txt", 'r') as arquivo:
    conteudo = arquivo.read
    conteudo = conteudo.lower()
    lista_arquivo = conteudo.split()
i = 0
for b in lista_arquivo:
    if b == "banana":
    	i += 1 
print (i)