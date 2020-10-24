def equaliza_imagem(x,k):
    a=len(x)
    i=0
    while i<a:
        if x[i]*k>225:
            x[i]=225
            i+=1
        else:
            x[i]*=k
            i+=1
    return x