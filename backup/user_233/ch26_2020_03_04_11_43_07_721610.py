valor_casa = float(input())
salario = float(input())
anos =  float(input())

prestacao = valor_casa / anos

if prestacao / salario > 0.3: print('Empréstimo não aprovado')
else: print('Empréstimo aprovado')