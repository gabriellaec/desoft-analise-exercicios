lista = ['','janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
a = str(input('mes'))
i = 0
while(i<=len(lista)):
    if a == lista[i]:
        print(i)
    i += 1