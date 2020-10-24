def equaliza_imagem(l, k):
    lista_equalizada = []
    for i in l:
        if i*k > 255:
            lista_equalizada.append(255)
        else:
            lista_equalizada.append(i*k)
    return lista_equalizada        
    