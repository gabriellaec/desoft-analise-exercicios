import json 
with open('estoque.json', 'r') as arq:
	file = arq.read()
dic = json.loads(file)

value  = 0
for price in dic['produtos']:
	value += price['quantidade']*price['valor']
print(value)