def lista_caracteres (x):
    l=[]
    i=0
    while i < len(x):
        if x[i] not in l:
            l.append(x[i])
            i+=1
    return l    