def encontra_maximo(matriz):
    linha_1 = matriz[0]
    linha_2 = matriz[1]
    linha_3 = matriz[2]
    max_linha_1 = max((linha_1), key=abs)
    max_linha_2 = max(linha_2, key=abs)
    max_linha_3 = max(linha_3, key=abs)
    lista_maximos = [max_linha_1, max_linha_2, max_linha_3]
    maior_n_absoluto = max(lista_maximos, key=abs)
    if maior_n_absoluto < 0:
        return maior_n_absoluto*(-1)
    else:
        return maior_n_absoluto