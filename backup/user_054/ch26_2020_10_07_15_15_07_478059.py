casa = float(input('valor da casa? '))
salário = float(input('salário? ' ))
anos = float(input('durante quantos anos quer pagar? ' ))

prestaçao = casa/(anos*12)

if prestaçao > 0.3*salário:
    print ('Empréstimo não aprovado')
else: 
    print ('Empréstimo aprovado')
