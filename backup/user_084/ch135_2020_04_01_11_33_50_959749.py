def equaliza_imagem(l,k):
    i=0
    e=[0]*len(l)
    while i<len(l):
        e[i]=l[i]*k
        if l[i]*k>255:
            e[i]=255
        i+=1
    return(e)
        
    
