def lista_caracteres(nrep):
    lis=[]
    i=0
    while i<len(nrep):
        if nrep[i] not in nrep:
            nrep[i].append(lis)
        i+=1      
    return lis