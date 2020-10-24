def estritamente_crescente(n):
    if n==[]:
        return n
    lista0=[]
    s=0
    i=1
    lista0.append(n[0])
    while i<len(n): 
        if n[i]>lista0[s]:
            s+=1
            lista0.append(n[i])
        i+=1
    return lista0    