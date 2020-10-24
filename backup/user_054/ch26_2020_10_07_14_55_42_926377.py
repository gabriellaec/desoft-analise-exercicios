casa = float(input(' valor da casa? '))
salário = float (input('salário? ' ))
meses = float (input('durante quantos anos quer pagar? ' ))

prestação = casa/meses

if salário < prestação:
    print ('Empréstimo aprovado')
else: 
    print ('Empréstimo não aprovado')
