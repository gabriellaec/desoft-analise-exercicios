with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
    
conteudo = conteudo.lower()
lista_palavras = conteudo.split()

i=0
for c in lista_palavras:
	if c == 'banana':
    	i+=1
print(i)