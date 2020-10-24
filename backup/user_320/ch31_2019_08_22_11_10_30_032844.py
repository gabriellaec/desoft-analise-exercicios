casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite quantos anos para pagar: '))

prestacao = casa / anos
limite = salario * .3

if prestacao > limite:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')