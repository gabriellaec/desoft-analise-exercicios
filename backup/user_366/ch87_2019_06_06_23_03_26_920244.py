import csv
with open("churras.txt", "r") as arquivo:
    leitor = csv.reader(arquivo)
    custo_total = 0
    for linha in leitor:
        custo_total += int(linha[1]) * float(linha[2])

print(custo_total)