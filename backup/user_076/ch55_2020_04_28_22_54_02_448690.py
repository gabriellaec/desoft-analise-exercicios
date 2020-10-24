def encontra_maximo (matriz):
    print(matriz)
    máximo_linha_1 = max(abs(matriz[0]))
    máximo_linha_2 = max(abs(matriz[1]))
    máximo_linha_3 = max(abs(matriz[2]))
    lista = [máximo_linha_1,máximo_linha_2,máximo_linha_3]
    máximo = max(lista)
    print(máximo)
    return máximo