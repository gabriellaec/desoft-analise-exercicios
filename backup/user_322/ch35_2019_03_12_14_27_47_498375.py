inicial = int(input("Qual o deposito inicial:?"))
mensal = int(input("Qual o deposito mensal:?"))
taxa = float(input("Qual a taxa de juros:?"))
taxa2 = taxa + 1
i = 0
if i > 0:
    juros = inicial * taxa2
    total = inicial + juros
    i = i + 1
    print("{0:.2f}".format(total))
    while i < 24:
        total = (total + mensal) * taxa2
        print("{0:.2f}".format(total))
        i = i + 1
total = (total + mensal) * taxa2
print("{0:.2f}".format(final))       
