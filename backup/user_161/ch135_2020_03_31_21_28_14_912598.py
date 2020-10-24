def equaliza_imagem(l, k):
    i = 0
    while i < len(l):
        l[i] *= k
        if l[i] > 255:
            l[i] = 255
        i += 1
    return l