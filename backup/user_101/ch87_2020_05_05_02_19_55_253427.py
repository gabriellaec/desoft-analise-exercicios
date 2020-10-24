with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    valor = 0
    for linha in linhas:
        l = linha.split(',')
        valor += float(l[1]) * float(l[2].strip())
print(valor)