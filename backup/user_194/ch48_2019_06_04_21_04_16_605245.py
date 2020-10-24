lista = ['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
mes = input('qual o nome do mes?')

i = -1
while i < len(lista):
    if lista[i] == mes:
        i += 1
        print(i)
    else:
        i+=1     