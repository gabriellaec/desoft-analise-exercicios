valor_da_casa = int(input("Qual o valor da casa? "))
salario = int(input("Qual o salário? "))
anos = int(input("Quantos anos? "))

if ((valor_da_casa)/(anos*12)) < salario*0.3:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')