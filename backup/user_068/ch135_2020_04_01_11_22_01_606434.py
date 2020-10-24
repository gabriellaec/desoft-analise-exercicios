def equaliza_imagem(a, k):
    i = 0
    b = []
    while i < 256:
        mult = a[i] * k
        if mult > 255:
            b.append(255)
        else:
            b.append(a[i]
        i += 1
    return b
    