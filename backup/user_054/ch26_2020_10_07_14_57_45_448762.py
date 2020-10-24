casa = float(input('valor da casa? '))
salário = float (input('salário? ' ))
meses = float (input('durante quantos meses quer pagar? ' ))

prestação = casa/meses

if prestação< 0.3*salário:
    print ('Empréstimo aprovado')
else: 
    print ('Empréstimo não aprovado')
