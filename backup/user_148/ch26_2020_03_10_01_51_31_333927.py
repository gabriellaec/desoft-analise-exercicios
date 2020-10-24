vc = float(input('Qual o valor da casa? '))
s = float(input('Qual o seu salário? '))
a = float(input('Em quantos anos você pagará essa casa? '))
p = vc/(a*12)
if p <= 0.3*s:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')