def classifica_lista(L):
    if len(L)<2:
        return 'nenhum'
    i=0
    while i in range(i,len(L)):
        while L[i]<=L[i+1]:
            i+=1
            if L[i]>L[i+1]:
                return 'nenhum'
            if i==len(L)-1:
                return 'crescente'
            
        while L[i]>=L[i+1]:
            i+=1
            if L[i]<L[i+1]:
                return 'nenhum'
            if i==len(L)-1:
                return 'decrescente'
        else:
            return 'nenhum'
        
            