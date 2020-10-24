def encontra_maximo(matriz):
    linha_1 = matriz[0]
    linha_2 = matriz[1]
    linha_3 = matriz[2]
    max_linha_1 = abs(max(linha_1))
    max_linha_2 = abs(max(linha_2))
    max_linha_3 = abs(max(linha_2))
    lista_maximos = [max_linha_1, max_linha_2, max_linha_3]
    maior_n_absoluto = abs(max(lista_maximos))
    return maior_n_absoluto