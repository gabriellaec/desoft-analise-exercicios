def equaliza_imagem(k,cores):
    i=0
    ls=[]
    n len(cores)
    while i<=n-1:
        if(cores[i]*k)>=255:
            ls.append(255)
        else:
            ls.append(cores[i]*k)
            i+=1
        return ls
 