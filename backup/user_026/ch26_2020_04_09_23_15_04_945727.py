valor= float(input("qual o valor da casa a se comprar? "))
salario= float(input("qual o seu salário? "))
quant_meses= float(input("em quantos meses deseja pagar? "))

prest_mensal = valor/quant_meses

if prest_mensal < salario*0.30:
    print('Empréstimo aprovado')
    
else:
    print('Empréstimo não aprovado')