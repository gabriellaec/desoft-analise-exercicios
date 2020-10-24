n_mes = int(input('qual o nome do mes'))

lista= ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

i = 0

while i < len(lista):
    if lista[i+1] == n_mes:
        print (i+1)
    i+=1    