valor_casa = float(input())
salario = float(input())
anos = int(input())

prestacao = valor_casa/(anos*12)

if prestacao > salario*0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')