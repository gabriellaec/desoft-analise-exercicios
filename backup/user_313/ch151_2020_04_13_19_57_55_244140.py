def classifica_lista(l1):

    cont = 0
    cont1 = 0
    if len(l1)>3:
        for i in range(0,len(l1)-1):
            if l1[i+1] > l1[i]:
                cont += 1
            else:
                break
            
        for i in range(0,len(l1)-1):
            if l1[i+1] < l1[i]:
                cont1 += 1
                
        
        if cont > 2 :
            return 'crescente'
        
        elif cont1 > 2 :
            return 'decrescente'
        
        elif cont < 2 :
            return 'nenhum'
        
        elif cont1 < 2 :
            return 'nenhum'
    if len(l1)<3:
        if len(l1) == 2:
            if l1[1]>l1[0]:
                return 'crescente'
            elif l1[1]< l1[0]:
                return 'descrescente'
            else:
                return'nenhum'