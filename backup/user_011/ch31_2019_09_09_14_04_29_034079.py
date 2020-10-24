valor_casa = float(input('Preço da casa? '))
salario = float(input('Seu salario? '))
tempo = float(input('Em quantos anos vai pagar? '))

prestacao = valor_casa/(tempo*12)

if prestacao > salario*0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')