valor_casa= float(input("Qual o valor da casa ?"))
salario= float(input("qual o seu salário?"))
anos_pagar = int(input("quantos anos para se pagar?"))

prestacao = valor_casa/(anos_pagar*12)

porcentagem_salario = 0.3*salario

if prestacao>porcentagem_salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')