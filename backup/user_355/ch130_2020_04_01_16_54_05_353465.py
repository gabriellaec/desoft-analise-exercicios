lista1=[]
def monta_mala (lista1):
    lista2= []
    i=0
    j=1
    while i<len(lista1):
        a=lista1[i]
        b=lista1[j]
        c=a+b
        if c<23:
            lista2.append(a)
            lista2.append(b)
        i+=1
        j+=1
    return lista2