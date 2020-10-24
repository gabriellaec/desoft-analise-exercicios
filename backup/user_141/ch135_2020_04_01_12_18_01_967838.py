def equaliza_imagem(k):
    lista= [10, 12, 100]
    lista_corrigida=[]*3
    lista_corrigida[0]= lista[0]*k
    lista_corrigida[1]= lista[1]*k
    lista_corrigida[2]= lista[2]*k
    return lista_corrigida
    print(equaliza_imagem(5))