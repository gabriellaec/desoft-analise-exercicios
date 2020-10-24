lista = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
i = 0
a = str(input('Mês = '))
while i <= len(lista):
    if a == lista[i]:
        print(i+1)
    i+=1