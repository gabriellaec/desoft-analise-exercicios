valor = float(input('Qual o valor da casa a comprar: '))
salario = float(input('Qual o valor do salário: '))
qntd_anos = float(input('Qual a quantidade de anos a pagar: '))

prestacao = valor/qntd_anos*12

if prestacao < salario*0.3:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')