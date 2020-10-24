def encontra_maximo (matriz):
    máximo_linha_1 = max(matriz[0])
    máximo_linha_2 = max(matriz[1])
    máximo_linha_3 = max(matriz[2])
    lista = [máximo_linha_1,máximo_linha_2,máximo_linha_3]
    máximo = max(lista)
    return máximo