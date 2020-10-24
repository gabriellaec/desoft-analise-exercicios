casa = int(input('Qual o valor da casa? '))
s = int(input('Qual o valor do salário? '))
n = int(input('Em quantos anos deseja pagar? '))

prest = casa / (n * 12)
sal = 0.3 * s
if prest <= sal:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')