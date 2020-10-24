def separa_trios(lista):
    s=lista[:3]
    trio=[]
    trio.append(s)
    i=3
    while i<len(lista):
        trio.append(lista[i:(i+3)])
        i+=3
    return trio