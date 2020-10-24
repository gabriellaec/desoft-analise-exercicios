inicial = float(input("Qual o deposito inicial:?"))
mensal = float(input("Qual o deposito mensal:?"))
taxa = float(input("Qual a taxa de juros:?"))
i = 1
total = inicial 
for i in range(24):
    inicial = inicial * (1+taxa) + mensal
    print("{0:.2f}".format(inicial)) 
print("{0:.2f}".format(inicial - total - 24 * mensal))