def total_do_semestre_por_bairro(dicio):
    listav=[]
    listab=[]
    for l,m in dicio.items():
        dicio[l]=sum(m[6:12])
        listav.append((m[6:12]))
        listab.append(l)
    a=max(listav)
    z=listav.index(a)
    
        
    return listab[z]