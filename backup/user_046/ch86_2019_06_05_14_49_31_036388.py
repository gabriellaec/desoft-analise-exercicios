with open('dados.csv','r') as arquivo:
	conteudo=arquivo.read()
    conteudo2=str(conteudo)
	for d in conteudo2:
		if conteudo2[d]==',':
			conteudo2[d]=='	'
	with open('dados.tsv','w') as arquivo2:
		tsv=arquivo2.write()
		tsv=conteudo2
        