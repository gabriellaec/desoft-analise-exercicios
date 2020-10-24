def separa_trios(lista):
    l=[]
    i=0
    while i in range(len(lista[i])):
        if (lista[i:i+3]) not in l and len(lista[i:i+3])==3:
            l.append(lista[i:i+3])
        i+=1
        return l
    