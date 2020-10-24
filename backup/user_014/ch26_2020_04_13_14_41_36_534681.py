valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário? '))
anos = int(input('Em quantos anos vai pagar? '))

prestação = int(valor_casa/ (anos * 12))

if prestação <= 0.3 * salario:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')
