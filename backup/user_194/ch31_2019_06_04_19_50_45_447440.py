valor_casa = float(input('qual o valor da casa?'))
salario = float(input('qual o salário?'))
anos = float(input('por quantos anos vai pagar?'))

prestação = valor_casa/(anos*12)

if prestação > 0.3*salario:
     print('Empréstimo não aprovado')
else:
     print('Empréstimo aprovado')