v=float(input('Valor da casa: '))
s=float(input('Salário: '))
a=float(input('Anos a pagar: '))
p=v*12/a
if p/s>0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')