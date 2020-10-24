valor=float(input('Qual o valor da casa?'))
tempo=int(input('Em quantos meses?'))
salario=float(input('Qual o seu salario'))
valor_mensal=valor/tempo
if valor_mensal < 0.3*salario:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')