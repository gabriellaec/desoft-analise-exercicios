a=float(input("valor da casa a comprar"))
b=float(input("salário"))
c=float(input("quantidades de anos a pagar"))
d=a/(12*c)
if d>b*0.3:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')