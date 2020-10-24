with open("churras.csv", "r") as arquivo:
    leitor = arquivo.read()
    custo_total = 0
    for linha in leitor:
        custo_total += int(linha[1]) * float(linha[2])

print(custo_total)