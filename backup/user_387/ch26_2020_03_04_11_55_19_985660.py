valor = float(input())
salario = float(input())
anos = float(input())

prest = valor/(anos * 12)

sal_30 = salario * 0.3

if sal_30 < prest:
    print('Empréstimo não aprovado')
    
else:
    print('Empréstimo aprovado')