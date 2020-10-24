v= float(input("valor da casa"))
s= float(input("salário"))
t= float(input("anos pra pagar"))
m= v/t/12

if m > 0.30*s:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')