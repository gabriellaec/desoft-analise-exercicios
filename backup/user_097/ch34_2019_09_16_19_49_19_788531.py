depositoInicial = float(input("Informe o valor do depósito inicial: "))
taxaJuros = float(input("Informe a taxa de juros: "))

montante = depositoInicial
m = 0
while (m < 24):
    montante = montante*(1+taxaJuros)
    m = m + 1
    print("{0:.2f}".format(montante))

totalGanho = montante - depositoInicial
print("{0:.2f}".format(totalGanho))