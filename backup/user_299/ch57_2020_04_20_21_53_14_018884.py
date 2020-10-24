def verifica_progressao(lista):
    r=[]
    q=[]
    pa = True
    pg = True

    for i,e in enumerate(lista):
        if i>0:
            r.append(lista[i]-lista[i-1])
            q.append(lista[i]/lista[i-1])
    
    dife = r[0]
    raza = q[0]

    for dif in r:
        if dif == dife and pa:
            pa == True
        else :
            pa == False

    for raz in q:
        if dif == dife and pg:
            pg == True
        else :
            pg == False
    
    if pa and pg:
        return 'AG'
    elif pa:
        return 'PA'
    elif pg:
        return 'PG'
    else:
        return 'NA'