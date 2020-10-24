def equaliza_imagem(a, k):
    i = 0
    b = []
    while i < len(a):
        mult = k * a[i]
        i += 1
        if mult > 255:
            b.append(255)
        else:
            b.append(mult)
        
    return b
    
    