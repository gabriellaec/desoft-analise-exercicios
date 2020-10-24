def equaliza_imagem(l,k):
    lista=[]
    i=0
    while i<len(l):
        c=l[i]*k
        if c<=255:
            lista.append(c)
        else:
            lista.append(255)
        i+=1
    return lista