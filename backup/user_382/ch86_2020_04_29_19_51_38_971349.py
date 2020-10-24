with open('dados.csv', 'r') as arq:
	file = arq.read().replace(',','    ')
	with open('dados.tsv', 'w') as arq2:
		new_file = arq2.write(file)
