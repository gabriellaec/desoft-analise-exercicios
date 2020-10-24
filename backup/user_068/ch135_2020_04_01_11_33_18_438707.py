def equaliza_imagem(a, k):
    i = 0
    b = [0]*255
    while i <= len(b):
        mult = k * a[i]
        if mult > 255:
            b.append(255)
        else:
            b.append(mult)
        i += 1
    return b
    