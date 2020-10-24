with open('dados.csv','r') as arquivo:
	conteudo=arquivo.read()
	with open('dados.tsv','w') as arquivo2:
		tsv=conteudo.write()
		for d in tsv:
            if d==',':
                d=='	'
     
        