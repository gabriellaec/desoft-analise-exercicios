with open('churras.txt', 'r') as arq:
	file = arq.readlines() 
preco = 0 
for i in file:
	item = i.split(',')
	preco += float(item[1])*float(item[2])
print(preco)





