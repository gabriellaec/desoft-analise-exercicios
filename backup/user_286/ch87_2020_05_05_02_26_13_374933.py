with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    total = 0

    for linha in linhas:
        linha = linha.split(',')
        total += (float(linha[1]) * float(linha[2]))

print(total)