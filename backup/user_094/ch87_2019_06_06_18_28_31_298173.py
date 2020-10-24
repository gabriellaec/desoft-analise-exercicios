import csv
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.read()
churras = conteudo.split(',')
total = 0
for i in range(len(churras)):
    if i%3==0:
        del churras[i]
for i in range(len(churras)):
	if i%2==0:
        preco = churras[i] * churras[i+1]
        total+=preco
print (total)
