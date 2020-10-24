with open('dados.csv','r') as arquivo:
	conteudo=arquivo.read()
    conteudo=str(conteudo)
	for d in conteudo:
		if conteudo[d]==',':
			conteudo[d]=='	'
	with open('dados.tsv','w') as arquivo2:
		tsv=arquivo2.write()
		tsv=conteudo
        