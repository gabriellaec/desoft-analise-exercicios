with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    valor = 0
    for linha in linhas:
        l = linha.split(',')
        valor += int(linha[1])*int(linha[2])
print(valor)