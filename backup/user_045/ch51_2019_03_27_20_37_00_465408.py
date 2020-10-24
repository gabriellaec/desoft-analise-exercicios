def estritamente_crescente(n):
    i=1
    s=0
    lista=[]
    lista[0]=n[0]
    while i<len(n):
        if n[i]>lista[s]:
            lista.append(n[i])
            s+=1
        i+=1
    return lista