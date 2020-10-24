valor_da_casa=input('Valor da casa a comprar: ')
salario=input('Salário: ')
quantidade_anos=input('Quantidade de anos a pagar: ')
prestacao_mensal= valor_da_casa/(quantidade_anos*12)

if prestacao_mensal<0.3*salario:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')
    