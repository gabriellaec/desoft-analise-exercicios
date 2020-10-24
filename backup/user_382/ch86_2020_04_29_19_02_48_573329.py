with open('dados.csv', 'r') as arquivo:
	conteudo = arquivo.read()
	with open('dados.tvs', 'w') as arquivo2:
	    conteudo = conteudo.replace(',', '	')
	    text = arquivo2.write(conteudo)

