def classifica_lista(x):
    if len(x)<2:
        return 'crescente'
    w = x[1]-x[0]
    if w>0:
        for i in range (len(x)-1):
            if x[i]-x[i+1]<=0:
                return 'nenhum'
    if w<0:
        for i in range (len(x)-1):
            if x[i]-x[i+1]>=0:
                return 'nenhum'
    if w==0:
        return 'nenhum'
    elif w<0:
        return 'decrescente'
    elif w>0:
        return 'crescente'