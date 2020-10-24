casa=input('Valor da casa a comprar:')
salario=input('Salário:')
tempo=input('Quantidade de anos:')
prestação=casa/(tempo*12)
if prestação>0.3*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')