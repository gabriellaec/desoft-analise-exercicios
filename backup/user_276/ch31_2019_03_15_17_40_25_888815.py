a = int(input('Valor da casa:  '))
b = int(input('Salário:   '))
c = int(input('Quantidade de anos:   '))
prestacao = a/(c*12)
sal = b*0.3
if prestacao < sal:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')