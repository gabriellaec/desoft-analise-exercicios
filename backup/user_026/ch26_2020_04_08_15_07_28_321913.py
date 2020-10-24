valor= int(input("qual o valor da casa a se comprar? "))
salario= int(input("qual o seu salário? "))
quant_meses= int(input("em quantos meses deseja pagar? "))

prest_mensal = valor/quant_meses

if prest_mensal<(salario/100)*30:
    print('Empréstimo aprovado')
    
if prest_mensal>(salario/100)*30:
    print('Empréstimo não aprovado')