lista = [1, 2, 3, -4, -5, 1, 2, 3]
tamanho = len(lista)

i = 0
while i < tamanho:
    if lista[i] < 0:
        lista[i] = 0
    i += 1