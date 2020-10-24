casa = input('Quanto custa a casa? ')
salario = input('Qual o seu salário? ')
anos = input('Em quantos anos vai pagar? ')

prestacao = casa/(anos*12)

if prestacao > salario * 0.3:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')
    