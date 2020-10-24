def mais_populoso(dicio):
    maior=[]
    listano=[]
    dicio1={}
    for el , val in dicio.items():
        for va in val.values():
            dicio1[el]=[]
        for vac in val.values():
            dicio1[el].append(vac)
    for e, v  in dicio1.items():
        maior.append(sum(v))
        listano.append(e)
    a=max(maior)
    z=maior.index(a)
        

    return listano[z]