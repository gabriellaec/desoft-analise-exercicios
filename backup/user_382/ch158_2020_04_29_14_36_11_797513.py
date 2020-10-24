with open ('texto.txt','r') as arquivo:
	conteudo = arquivo.read()

conteudo = conteudo.split()
print(len(conteudo))

