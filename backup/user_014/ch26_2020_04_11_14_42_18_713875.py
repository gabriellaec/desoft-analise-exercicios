valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário? '))
anos = int(input('Em quantos anos vai pagar? '))

prestação = (valor_casa)/ (anos * 12)

if prestação > salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')