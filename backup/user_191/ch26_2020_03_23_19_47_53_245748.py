v=float(input('Valor da casa: '))
s=float(input('Salário: '))
a=float(input('Anos a pagar: '))
p=v/a*12
if p/s>0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')