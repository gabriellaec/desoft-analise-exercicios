meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
nome = input('Qual o nome do mes? ')
index = 0
while nome != meses[index]:
    index += 1

print (meses[index])