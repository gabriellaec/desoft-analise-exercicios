deposito_inicial= int(input('Qual o deposito inicial? '))
taxa_de_juros = 0.01*int(input('Qual a taxa de juros? '))
mes = 0
while mes <24:
    mes += 1
    valor_atual = deposito_inicial*(1+taxa_de_juros)**mes
    print('você possui {0} na conta'.format(valor_atual))
    
print('você lucrou {0} com seus investimnentos'.format(valor_atual-deposito_inicial))