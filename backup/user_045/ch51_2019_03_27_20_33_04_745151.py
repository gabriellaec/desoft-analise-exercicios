def estritamente_crescente(n):
    i=1
    lista=[]
    lista[0]=n[0]
    while i<len(n):
        if n[i]>n[i-1]:
            lista.append(n[i])
        i+=1
    return lista