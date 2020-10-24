def  junta_nome_sobrenome(l1,l2):
    l3 = []
    i = 0
    #j = []
    #j[0] = [ ]
    while i < len(l1):
        l3.append(l1[i]+ ''' '''+l2[i])
        i += 1
    return l3