depositoInicial = float(input("Informe o valor do depósito inicial: "))
taxaJuros = float(input("Informe a taxa de juros: "))

montante = 0
m = 0
while (m < 25):
    montante = (depositoInicial*((1+taxaJuros)**m))
    m = m + 1
    print(round(montante, 2))

totalGanho = montante - depositoInicial
print(round(totalGanho, 2))