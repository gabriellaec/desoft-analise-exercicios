def equaliza_imagem(l,k):
    i=0
    e=[]*len(l)
    while i<len(l)-1:
        e[i]=l[i]*k
        i+=1
    return(e)
    
