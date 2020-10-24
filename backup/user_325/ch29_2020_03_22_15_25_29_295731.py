di = float(input("Digite o deposito inicial: "))
tx = float(input("Digite a taxa de juros adotada: "))
mes = 1
while mes <= 24:
    tot = di*((1+tx)**mes)
    print("O valor do mes {0} é {1:.2f}".format(mes,tot))
    mes += 1
print("O valor total do periodo é {0}".format(tot))