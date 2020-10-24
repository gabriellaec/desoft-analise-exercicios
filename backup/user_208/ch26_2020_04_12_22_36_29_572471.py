valor_da_casa = int(input("Qual o valor da casa? "))
salario = int(input("Qual o seu salário? "))
anos = int(input("Em quantos anos a casa será paga? "))
meses = anos*12
prestacao_mensal = valor_da_casa/meses
porcentagem_salario = salario*0.3
if  prestacao_mensal > porcentagem_salario:
    print ("Empréstimo não aprovado.")
else:
    print ("Empréstimo aprovado.")
     
