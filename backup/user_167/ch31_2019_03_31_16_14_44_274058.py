a=float(input("valor da casa a comprar"))
b=float(input("salário"))
c=float(input("quantidades de anos a pagar"))
d=a/(12*c)
if d>0.3*b:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')