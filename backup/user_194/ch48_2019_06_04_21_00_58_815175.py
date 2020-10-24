lista = ['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
mes = input('qual o nome do mes?')

i = 0
while i < len(lista-1):
    if lista[i] == mes:
        i += 1
        print(i)
    else:
        i+=1
       