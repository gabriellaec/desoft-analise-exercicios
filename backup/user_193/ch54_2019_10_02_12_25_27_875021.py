def junta_nome_sobrenome(l1, l2):
    i=0
    l=[]
    while i<len(l1):
        l.append(l1[i]+" "+l2[i])
        i+=1
    return l