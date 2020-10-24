d_inicial = int(input("Qual depósito inicial? "))
d_mensal = int(input("Qual o valor dos depósitos mensais? "))
taxa = float(input("Qual a taxa de juros aos mês(em porcentagem)?"))
taxa_real = (taxa/100) + 1
conta = d_inicial

i = 0
while i < 30:
    if i > 0:
        conta += d_mensal
    print("No mês de número {0} você tem R$ {1:.2f} em sua conta".format(i, conta))
    conta = conta * taxa_real
    i += 1