depósito_inicial = int(input('depósito inicial'))
taxa_de_juros = int(input('taxa de juros'))
i = 1
M = 0
while i <= 24:
    M = depósito_inicial*(1+taxa_de_juros)**i
    print('Para o {} mês montante igual a {}'.format(i,M))
    i += 1
J = M - depósito_inicial     
print(J)