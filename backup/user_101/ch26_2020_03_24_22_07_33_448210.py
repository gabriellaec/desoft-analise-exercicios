valor_da_casa = input("Qual o valor da casa a comprar? ")
salario = int(input("Qual o seu salário? "))
anos_a_pagar = int(input("Em quantos anos você deseja pagar? "))
prestacao = valor_da_casa/(anos_a_pagar*12)

if prestacao>(0.3*salario):
    print ("Empréstimo não aprovado")
else:
    "Empréstimo aprovado"