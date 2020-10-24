import json 
with open('estoque.json', 'r') as arq:
	file = arq.read()
dic = json.loads(file)

valor = 0 
lista_valores = []

for sub_dic1 in dic:
	for v in sub_dic1:
		lista_valores.append(sub_dic1[v])

for i in range(len(lista_valores)-1):
	valor += lista_valores[i+1]*lista_valores[i]

print(valor)

