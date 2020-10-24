def equaliza_imagem(i,k):
    n=0
    y=len(i)
    while n<y:
        x=(i[n])
        i[n]=x*k
        n=n+1
        if x*k>250:
            i[n]=250