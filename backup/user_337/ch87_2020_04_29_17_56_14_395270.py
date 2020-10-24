with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    valor = 0
    for linha in linhas:
        lista = linha.split(',')
        valor = valor + (float(lista[1]) * float(lista[2]))
print(valor)