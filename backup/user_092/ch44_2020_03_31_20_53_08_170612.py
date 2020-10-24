lista = ['','janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
a = str(input('mes'))
i = 1
while(i < 12):
    if a == lista[i]:
        print(i)
    else:
        i += 1