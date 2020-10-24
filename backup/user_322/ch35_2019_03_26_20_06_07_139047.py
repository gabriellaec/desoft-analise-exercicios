inicial = float(input("Qual o deposito inicial:?"))
mensal = float(input("Qual o deposito mensal:?"))
taxa = float(input("Qual a taxa de juros:?"))
i = 1
total = inicial
while i <= 24:
	total = total + (total * (taxa/100)) + mensal
    print("{0:.2f}".format(total)) 
    i = i + 1
final = total - (inicial + (mensal * 23))
print("{0:.2f}".format(final)) 