def calcula_valor_devido(valoremp, meses, taxa):
    x=(valoremp*((1+(taxa/100))**meses))
    return x

valoremp=float(input('Qual é o valor emprestado? '))
meses=int(input('Quantos meses? '))
taxa=float(input('Qual é a taxa de juros? '))
print('O valor devido é {:.2f} reais!'.format(calcula_valor_devido(valoremp, meses, taxa)))
