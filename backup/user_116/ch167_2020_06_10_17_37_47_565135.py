def bairro_mais_custoso(dicio):
    listav=[]
    listab=[]
    for l,m in dicio.items():
        dicio[l]=sum(m[6:12])
        listav.append(sum(m[6:12]))
        listab.append(l)
    a=max(listav)
    z=listav.index(a)
    
        
    return listab[z]