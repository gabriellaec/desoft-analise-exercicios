valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario? '))
anos = float(input('Vai pagar em quantos anos? '))

prestacao = valor/(anos*12)

if prestacao > salario*0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
