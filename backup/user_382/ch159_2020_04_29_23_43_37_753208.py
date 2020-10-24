import json 
with open('estoque.json', 'r') as arq:
	file = arq.read()
dic = json.loads(file)

valor = 0 

for key in dic:
	lista_dic = dic[key]

lista_valores = []

for dics in lista_dic:
	for key in dics:
		lista_valores.append(dics[key])

for i in range(0,len(lista_valores),3):
	valor += lista_valores[i+1]*lista_valores[i+2]

print(valor)





