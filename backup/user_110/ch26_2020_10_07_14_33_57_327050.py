valor_casa = int(input("qual o valor da casa a comprar?" ))
salario = int(input("qual o seu salario?"))
anos = int(input("quantos anos para pagar?"))

valor_prestacao = valor_casa/(anos*12)

if valor_prestacao > salario*0.30:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')