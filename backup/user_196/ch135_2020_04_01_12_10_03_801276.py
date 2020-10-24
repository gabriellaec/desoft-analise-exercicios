def equaliza_imagem(p,k):
    p = [l]*255
    while l >= 0 and l<=255:
        c = []
        i=0
        while i < len(p):
            j = p[i]*k
            i+=1
            c.append(j)
    return c