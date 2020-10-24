v=float(input('Valor da casa a comprar: '))
s=float(input('Salário: '))
t=float(input('Quantidade de anos a pagar: '))

if v/(12*t)>0.3*s:
    print ('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')