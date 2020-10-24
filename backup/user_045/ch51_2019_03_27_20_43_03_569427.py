
def estritamente_crescente(n):
    i=1
    s=0
    lista=[]
    lista[0]=n[0]
    while i-1<len(n):
        if n[i]>lista[s]:
            s+=1
            lista[s]=n[i]
        i+=1
    return lista