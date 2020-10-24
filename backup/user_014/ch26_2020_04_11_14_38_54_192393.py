valor_casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o salário? '))
anos = int(input('Em quantos anos vai pagar? '))

prestação = (valor_casa)/ (anos * 12)

if prestação > salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')