mes = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
n = int(input('digite um número de mes:'))

i = 0 

while i < len(mes):
    if n == i:
        print(mes[i-1])
    i += 1