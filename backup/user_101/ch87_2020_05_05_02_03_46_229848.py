with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    valor = 0
    for linha in linhas:
        l = linha.split(',')
        valor += linha[1]*linha[2]
print(valor)