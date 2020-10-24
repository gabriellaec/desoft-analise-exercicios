with open ("dados.csv", 'r')as arquivo:
    conteudo = arquivo.read()

tsv = "	".join(conteudo.split(','))

with open('dados.tsv','w') as arquivo:
	arquivo.write(tsv)
