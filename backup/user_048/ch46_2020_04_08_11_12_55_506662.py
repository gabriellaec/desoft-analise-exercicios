def numero_no_indice (liste):
    listr=[]
    o=0
    for e in liste:
        if e==o:
            listr.append(e)
        o+=1
    return listr

def numero_no_indice(lista):
    listt=[]
    i=0
    while i <len(lista):
        if lista[i]==i:
            listt.append(lista[i])
        i+=1
    return listt

