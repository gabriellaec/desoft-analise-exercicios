x = input('digite o nome do mês: ')
z = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
for i in range(len(z)):
    if z[i]==x:
        print(i+1)