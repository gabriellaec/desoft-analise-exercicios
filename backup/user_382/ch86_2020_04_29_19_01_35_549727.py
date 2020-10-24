with open('dados.txt', 'r') as arquivo:
	conteudo = arquivo.read()
	open with('dados.tvs', 'w') as arquivo2:
	conteudo = conteudo.replace(',', '\t')
	text = arquivo2.write(conteudo)

