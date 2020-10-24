depositoInicial = float(input("Informe o depósito inicial:"))
depositoMensal =  float(input("Informe o depósito mensal:"))
taxaJuros = float(input("Informe a taxa de juros:"))

montante = depositoInicial
m = 0
while (m < 24):
    montante = montante*(1+taxaJuros)
    montante = montante + depositoMensal
    print("{0:.2f}".format(montante))
    m = m +1

totalGanho = montante-depositoInicial
print("{0:.2f}".format(totalGanho))