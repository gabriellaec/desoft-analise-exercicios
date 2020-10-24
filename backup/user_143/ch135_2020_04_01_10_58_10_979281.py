def equaliza_imagem(l,k):
    lista=[]
    i=0
    while i<len(l):
        k=l[i]*k
        if k<=255:
            lista.append(k)
        else:
            lista.append(255)