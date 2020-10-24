def estritamente_crescente(n):
    i=0
    lista=[]
    lista[i]=n[i]
    while i<len(n):
        if n[i]>n[i-1]:
            lista.append(n[i])
        i+=1
    return lista