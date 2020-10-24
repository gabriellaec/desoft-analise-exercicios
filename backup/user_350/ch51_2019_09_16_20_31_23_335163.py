def estritamente_crescente(n):
    i=0
    m=n[]
    lista=[]
    while i<len(n):
        if n[i]>m:
            m = n[i]
            lista.append(n[i])
        i+=1
    return lista
        