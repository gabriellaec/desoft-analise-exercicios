def classifica_lista (l):
    if len(l)<2:
        return 'nenhum'
    else:
        maior=0
        maior=l[0]
        i=1
        cc=0
        cd=0
        while i<len(l):
            if maior>l[i]:
                cd+=1
            elif maior<l[i]:
                cc+=1
            maior=l[i]
            i+=1
        if cc==len(l)-1:
            return 'crescente'
        elif cd==len(l)-1:
            return 'decrescente'
        else:
            return 'nenhum'
        
        