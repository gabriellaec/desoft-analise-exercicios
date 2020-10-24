capital = float(input("deposito inicial: "))
juros = float(input("taxa de juros: "))
meses = 0
while meses < 25:
    montante = capital * ((1 + juros) ** meses)
    print(montante)
    meses += 1
    montante_soma = montante + montante
print(montante_soma)
    