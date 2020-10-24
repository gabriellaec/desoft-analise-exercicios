def classifica_lista(L):
    if len(L)<2:
        return 'nenhum'
    i=0
    while i in range(i,len(L)):
        if L[i]<=L[i+1]:
            i+=1
            while L[i]<=L[i+1]:
                i+=1
                if i==len(L)-1:
                    return 'crescente'
        if L[i]>=L[i+1]:
            i+=1
            while L[i]>=L[i+1]:
                i+=1
                if i==len(L)-1:
                    return 'decrescente'
        else:
            return 'nenhum'
        
            