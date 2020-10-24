inicial = float(input("Qual o deposito inicial:?"))
mensal = float(input("Qual o deposito mensal:?"))
taxa = float(input("Qual a taxa de juros:?"))
i = 0
total = inicial * taxa
while i <= 24:
    if i == 0:
        print("{0:.2f}".format(inicial))
        i = i + 1
    if i == 1:
        print("{0:.2f}".format(total))
        i = i + 1
    else:
        total = (total + mensal) * taxa
        print("{0:.2f}".format(total))
        i = i + 1
