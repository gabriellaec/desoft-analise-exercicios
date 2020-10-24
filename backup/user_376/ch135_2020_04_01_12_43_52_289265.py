def equaliza_imagem(lista,k):
    n=0
    tamanho=len(lista)
    while n<tamanho:
        x=(lista[n])
        lista[n]=x*k
        if x*k>255:
            lista[n]=(255)
            n=n+1
        else:
            n=n+1
    return lista