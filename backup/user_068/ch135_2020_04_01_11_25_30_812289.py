def equaliza_imagem(a, k):
    i = 0
    b = [0]*255
    while i <= len(b):
        mult = a[i] * k
        if mult > 255:
            b.append(255)
        else:
            b.append(a[i])
        i += 1
    return b
    