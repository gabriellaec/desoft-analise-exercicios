def equaliza_imagem(p,k):
    c = []
    i=0
    while i < len(p):
        j = p[i]*k
        i+=1
        c.append(j)
    return c