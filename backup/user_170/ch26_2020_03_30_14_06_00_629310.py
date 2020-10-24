v = float(input('Qual o valor da casa? '))
s = float(input('Qual o salario? '))
a = float(input('Quantos anos para pagar? '))
m = a *12
p = v/a

if p > (0.3*a):
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')