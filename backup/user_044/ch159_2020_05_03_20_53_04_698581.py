import json

with open('estoque.json', 'r') as arquivo:
	conteudo=arquivo.read()
	estoque=json.loads(conteudo)
	valor=0

	for i in estoque["produtos"]:
		valor+=i["quantidade"]*i["valor"]

	print(valor)