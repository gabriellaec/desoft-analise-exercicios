inicial = float(input("Qual o deposito inicial:?"))
mensal = float(input("Qual o deposito mensal:?"))
taxa = float(input("Qual a taxa de juros:?"))
i = 1
total = inicial 
while i <= 24:
    inicial = inicial * (1+taxa) + mensal
    print("{0:.2f}".format(inicial)) 
    i = i + 1
final = inicial - total - 24 * mensal
print("{0:.2f}".format(final))