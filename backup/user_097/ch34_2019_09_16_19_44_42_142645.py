depositoInicial = float(input("Informe o valor do depósito inicial: "))
taxaJuros = float(input("Informe a taxa de juros: "))

montante = 0
m = 0
while (m < 25):
    montante = (depositoInicial*((1+taxaJuros)**m))
    m = m + 1
    print("Valor:", round(montante, 2))

totalGanho = montante - depositoInicial
print("Total ganho:", round(totalGanho, 2))