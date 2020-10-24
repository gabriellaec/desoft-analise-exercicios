def separa_trios (nomes):
    lista=[]
    i=0
    while i<len(nomes):
        trio=nomes[i:i+3]
        lista.append(trio)
        i+=3
    return lista