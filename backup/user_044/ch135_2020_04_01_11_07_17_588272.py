def equaliza_imagem(lista,k):
    ls=[]
    i=1
    n=len(lista)
    while i<=n:
        if (lista[i]*k)>=255:
            ls.append(255)
        else:
            ls.append(lista[i]*k)
        i+=1
    return ls     