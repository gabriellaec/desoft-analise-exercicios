with open('dados.csv','r') as arquivo:
	conteudo = arquivo.read()
with open('dados.tsv','w') as novoarquivo:
	novoarquivo.write(print(conteudo))