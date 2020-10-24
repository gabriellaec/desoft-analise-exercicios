def classifica_lista(l):
    if len(l)<2:
        return 'nenhum'
    z = l[1]-l[0]
    if z>0:
        for i in range (len(l)-1):
            if l[i+1]-l[i]<=0:
                return 'nenhum'
    if z<0:
        for i in range (len(l)-1):
            if l[i+1]-l[i]>=0:
                return 'nenhum'
    if z==0:
        return 'nenhum'
    elif z<0:
        return 'decrescente'
    elif z>0:
        return 'crescente'
    