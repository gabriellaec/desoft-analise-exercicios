dep_inicial = float(input("Qual o depósito inicial?"))
juros_anual = float(input("Qual a taxa de juros anual da poupança em porcentagem?"))

juros_mensal = (1 + juros_anual) ** (1/12) - 1

n = 0

while n < 24:
    n += 1
    total = dep_inicial * (1 + juros_mensal) ** n - dep_inicial
    print("{0:.02f}".format(total))

lucro = dep_inicial * (juros_mensal + 1) ** 24 - dep_inicial
print("{0:.02f}".format(lucro))