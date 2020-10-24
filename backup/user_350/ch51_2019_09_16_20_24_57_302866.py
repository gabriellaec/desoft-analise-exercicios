def estritamente_crescente(n):
    i=0
    m=n[0]
    lista=[n[0]]
    while i<len(n):
        if n[i]>m:
            m = n[i]
            lista.append(n[i])
        i+=1
    return lista
        