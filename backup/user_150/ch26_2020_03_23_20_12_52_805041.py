valor = float (input('Quanto custa a casa?'))
salario = float (input('Qual o salário mensal dos trabalhadores? '))
anos = float (input('Quantos anos você vai pagar? '))

if valor/(anos*12) > (30/100)*salario:
    print('Empréstimo não aprovado')
elif valor/(anos*12) <= (30/100)*salario:
    print('Empréstimo aprovado')