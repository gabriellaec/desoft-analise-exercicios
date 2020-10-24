def classifica_lista (l1):
    
    if len(l1)==1 or l1==[]:
        return "nenhum"
    else:
        for i in range(len(l1)-1):
            if l1[i+1] < l1[i]:
                return "decrescente"
            elif l1[i+1] > l1[i]:
                return "crescente"
            else:
                return "nenhum"