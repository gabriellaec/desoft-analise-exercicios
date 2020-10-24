valor_da_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o salário? "))
anos = float(input("Quantos anos "))

if (valor_da_casa/(anos*12))*0.3 <= salario:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')