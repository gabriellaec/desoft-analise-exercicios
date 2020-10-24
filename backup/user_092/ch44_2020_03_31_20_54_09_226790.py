lista = ['','janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
a = str(input('mes'))
i = 1
roda = True
while(roda):
    if a == lista[i]:
        print(i)
    i += 1
    else:
        roda = False