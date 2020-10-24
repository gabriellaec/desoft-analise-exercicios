valor_da_casa = float(input('Digite o valor da casa: R$ '))
print('---------------------------------------------------------------')


salario = float(input('Digite o valor do salário: R$ '))
print('---------------------------------------------------------------')


anos_para_pagar = float(input('Digite o total de anos para pagar: R$ '))
print('---------------------------------------------------------------')

prestacao = valor_da_casa/(12*anos_para_pagar)

if prestacao > 0.3*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')