def separa_trios (nomes):
    trio=[]
    i=0
    while i<len(lista):
        stg=nomes[i]+nomes[i+1]+nomes[1+2]
        if nomes[i+2] not in nomes:
            stg=nomes[i]+nomes[i+1]
        elif nomes[i+1] and nomes[i+2] not in nomes:
            stg=nome[i]
        i+=3
        trio.append(stg)
    return trio