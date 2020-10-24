a=float(input("valor da casa a comprar"))
b=float(input("salário"))
c=float(input("quantidades de anos a pagar"))
e=a/c
if(e<=b*0.3):
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')