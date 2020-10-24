a=float(input("valor da casa a comprar:"))
b=float(input("salario:"))
c=float(input("quantidade de anos a pagar":))
y=a/c

if y <= 0.3*b:
    print ('Empréstimo aprovado')
else:
    print ('Empréstimo não aprovado' )
    
