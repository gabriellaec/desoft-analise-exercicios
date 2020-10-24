with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        lista = linha.split(',')
        valor = valor + (lista[1] * lista[2])
print(valor)