with open('churras.txt', 'r') as arq:
	file = arq.readlines()
soma = 0 
preco = 0 
for i in file:
	item = i.split(',')
	preco += item[1]*item[2]
print(preco)





