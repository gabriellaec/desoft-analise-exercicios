def inverte_dicionario(idades):
    idades2={}
    for pessoas in idades:
        i=idades[pessoas]
        if not i in idades2:
            idades2[i]=[]
            idades2[i].append(pessoas)
        else:
            idades2[i].append(pessoas)
    return idades2
   
        