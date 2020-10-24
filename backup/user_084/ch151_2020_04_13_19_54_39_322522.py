def classifica_lista(l):
    l=[]
    if len(l)<2:
        return('nenhum')
    else:
        if l[0]>l[1]:
            return('decrescente')
        elif l[0]<l[1]:
            return('crescente')
        else:
            return('nenhum')
        
    
    