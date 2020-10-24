dep_ini = float(input("Digite o depósito inicial: "))
tax_jur = float(input("Digite a taxa de juros da sua poupança: "))
i = 1
soma = 0
while i <= 24:
    total = dep_ini*tax_jur
    soma += total
    print("{0:.2f}".format(soma))
    i += 1
print("{0:.2f}".format(soma))
