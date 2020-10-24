def classifica_lista(l1):
    conta = 0
    conta1 = 0
    if len(l1) == 0:
        return 'nenhum'

    if len(l1) == 1:
        return 'nenhum'
    if len(l1)>3:
        for i in range(0,len(l1)-1):
            if l1[i+1] > l1[i]:
                conta+=1
            else:
                conta-=1
        for i in range(0,len(l1)-1):
            if l1[i+1] < l1[i]:
                conta1 +=1
            else:
                conta1 -=1
                
        if conta < 2 and conta1 < 2:
            return'nenhum'
        elif conta >= 2:
            return 'crescente'
        elif conta1 >= 2:
            return 'decrescente'
    if len(l1)<3:
        if len(l1) == 2:
            if l1[1]>l1[0]:
                return'crescente'
            elif l1[1]<l1[0]:
                return'decrescente'
            else:
                return'nenhum'