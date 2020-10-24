v = float(input('Qual o valor da casa? '))
s = float(input('Qual o salario? '))
a = float(input('Quantos anos para pagar? '))

p = v/a

if p > (0.3*s):
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')