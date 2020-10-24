n_mes = int(input('qual o número do mes'))
a=n_mes-1

lista= ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

i = 0

while i < len(lista):
    if i == a:
        print (lista[i])
    i+=1    
       

    