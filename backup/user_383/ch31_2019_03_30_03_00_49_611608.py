valor=float(input('Qual o valor da casa?'))
salario=float(input('Qual o seu salario'))
tempo=int(input('Em quantos meses?'))

valor_mensal=valor/tempo
if valor_mensal >= 0.3*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')