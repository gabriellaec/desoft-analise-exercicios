deposito = float(input("Qual o depósito inicial?"))
taxa = float(input("Qual a taxa de juros?"))
mes = 1
soma = 0

while mes <= 24:
    juros = deposito*(1+taxa)**mes - deposito
    print ("Os juros no mês {0} foi de {1: .2f} reais". format(mes, juros))
    mes += 1
    soma += juros

print("O total ganho com juros foi de {0: .2f} reais". format(soma))