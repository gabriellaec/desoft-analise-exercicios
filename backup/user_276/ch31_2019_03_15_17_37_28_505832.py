a = int(input('Valor da casa:  '))
b = int(input('Salário:   '))
c = int(input('Quantidade de anos:   '))
prestacao = a/c*12
if prestacao < 0,3*b:
    return 'Empréstimo aprovado'
else:
    return 'Empréstimo não aprovado'