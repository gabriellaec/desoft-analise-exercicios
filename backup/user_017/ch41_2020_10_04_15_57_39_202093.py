def zera_negativos(n):
    tamanho = len(n)
    i=0
    while i < tamanho:
        if n[i]<0:
            n[i]=0
    i=i+1
    return n