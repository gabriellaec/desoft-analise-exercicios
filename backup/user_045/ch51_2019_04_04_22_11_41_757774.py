
def estritamente_crescente(n):
    if n==[]:
        return n
    i=1
    s=0
    lista=[]
    lista.append(n[0])
    while i<len(n):
        if n[i]>lista[s]:
            s+=1
            lista.append(n[i])
            
        i+=1
    return lista