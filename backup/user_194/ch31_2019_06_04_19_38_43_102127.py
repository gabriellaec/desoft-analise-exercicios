valor_casa = int(input('qual o valor da casa?')
salario = int(input('qual o salário?')
anos = int(input('por quantos anos vai pagar?')

prestação = valor_casa/(anos/12)

if prestação > 0.3*salario:
     print('Empréstimo não aprovado')
else:
     print('Empréstimo aprovado')