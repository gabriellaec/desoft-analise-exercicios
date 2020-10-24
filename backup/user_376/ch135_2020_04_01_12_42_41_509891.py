def equaliza_imagem(i,k):
    n=0
    y=len(i)
    while n<y:
        x=(i[n])
        i[n]=x*k
        if x*k>255:
            i[n]=(255)
            n=n+1
        else:
            n=n+1
    return i