deposito = int(input("Qual o valor do deposito:?"))
juros = float(input("Qual a taxa de juros:?"))       
i = 1
total = 0
while i < 25:
    valor_mes = deposito * (juros) ** i
    print("{0:.2f}".format(valor_mes))
    i = i + 1
    total = valor_mes - deposito
print("{0:.2f}".format(total))
    