dep_inicial = float(input("Qual o depósito inicial?"))
juros = float(input("Qual a taxa de juros mansal da poupança?"))

n = 0

while n < 24:
    n += 1
    total = dep_inicial * (1 + juros) ** n - dep_inicial
    print("{0:.02f}".format(total))

lucro = dep_inicial * (juros + 1) ** 24 - dep_inicial
print("{0:.02f}".format(lucro))