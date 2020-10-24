def equaliza_imagem(l, k):
    l = list(map(lambda x: x*k, l))
    return list(map(lambda x: 255 if x > 255 else x, l))
        