casa = int(input('Quanto custa a casa? '))
salario = int(input('Qual o seu salário? '))
anos = int(input('Em quantos anos vai pagar? '))

prestacao = casa/(anos*12)

if prestacao > salario * 0.3:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')
    