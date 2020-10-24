n = int(input('Qual o numero do mes?'))

while n <= 12:
    meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    nome = meses[n-1]
    print(nome)
    break 
    
    