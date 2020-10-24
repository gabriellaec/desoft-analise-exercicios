def lista_caracteres(nrep):
    lis=[]
    i=0
    while i<len(nrep):
        if nrep[i] not in lis:
            nrep[i].append(lis)
        i+=1      
    return lis