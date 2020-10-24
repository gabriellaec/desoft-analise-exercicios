v=float(input('valor da casa: '))
s=float(input('salario: '))
a=float(input('Quantidade de anos para pagar: '))
vp=v/(12*a)
if vp > 0.3*s:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')