deposito = float(input("Qual é o depósito inicial? "))
taxa = float(input("Qual é a taxa de juros? "))

contador = 1
montante = 0
while contador <= 24:
    montante = deposito * (1 + taxa) ** contador
    print("Para o {0:.2f} mês igual a {1:.2f}".format(contador, montante))
    contador += 1
total_ganho = montante - deposito
print(total_ganho)