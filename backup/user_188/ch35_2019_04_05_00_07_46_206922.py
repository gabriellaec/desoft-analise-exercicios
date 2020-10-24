deposito_inicial = float(input("Qual é o depósito inicial? "))
deposito_mensal = float(input("Qual é o depósito mensal? "))
taxa = float(input("Qual é a taxa de juros? "))

novo_dep = deposito_inicial + deposito_mensal
contador = 1
montante = deposito_inicial * (1 + taxa)
while contador <= 24:
    montante = novo_dep * (1 + taxa) ** contador
    deposito_mensal = float(input("Qual é o depósito mensal? "))
    novo_dep += deposito_mensal
    print("Para o {0:.2f} mês igual a {1:.2f}".format(contador, montante + deposito_mensal))
    contador += 1
total_ganho = montante - deposito
print(total_ganho)