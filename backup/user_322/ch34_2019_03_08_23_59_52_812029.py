deposito = int(input("Qual o valor do deposito:?"))
juros1 = float(input("Qual a taxa de juros:?"))   
juros2 = juros1 + 1
i = 1
total = 0
while i < 25:
    valor_mes = deposito * (juros2) ** i
    print("{0:.2f}".format(valor_mes))
    i = i + 1
    total = valor_mes - deposito
print("{0:.2f}".format(total))
    