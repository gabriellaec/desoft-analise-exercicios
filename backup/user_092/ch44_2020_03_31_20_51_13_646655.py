lista = ['','janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
a = str(input('mes'))
i = 0
while(i < 11):
    if a == lista[i]:
        print(i)
    i += 1