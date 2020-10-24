def equaliza_imagem(x,k):
    a=len(x)
    i=0
    while i<a:
        if x[i]*k>255:
            x[i]=255
            i+=1
        else:
            x[i]=x[i]
            x[i]*=k
            i+=1
    return x