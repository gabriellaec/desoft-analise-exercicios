def separa_trios(nomes):
    i=0
    trio=[]
    while i < len(nomes):
        fatiamento= nomes[i:i+3]
        trio.append(fatiamento)
        i+=3
    return(trio)