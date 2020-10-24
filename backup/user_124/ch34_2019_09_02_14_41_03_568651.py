capital = float(input("deposito inicial: "))
juros = float(input("taxa de juros: "))
meses = 0
while meses < 24:
    montante = capital * ((1 + juros) ** meses)
    print(montante)
    meses += 1
    capital = capital + montante
print(capital)
    