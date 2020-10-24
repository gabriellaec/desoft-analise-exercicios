contador = 1
deposito_inicial=float(input('Qual o valor do depósito inicial?'))
taxa_juros=float(input('Qual a taxa de juros da poupança?'))
while contador<=24:
    print(deposito_inicial+deposito_inicial*taxa_juros*contador)
    contador+=1