def separa_trios(lista):
    i=0
    l=[]
    while i<len(lista):
        l.append(lista[i:i+3])
        i+=3
    return l
    