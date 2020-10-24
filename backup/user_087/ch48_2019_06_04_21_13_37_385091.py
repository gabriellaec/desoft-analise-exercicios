meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
nome = input('Qual o nome do mes?')
i = 0
while i < 12:
    if nome == meses[i]:
        print(i+1)
    i += 1
 