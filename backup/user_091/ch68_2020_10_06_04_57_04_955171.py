def separa_trios(lista):
    lista1=[]
    if len(lista)==1:
        lista1=[lista]
        return lista1
    else:
        i=0
        while i<len(lista):
            lista1.extend(lista[i:i+3])
            i+=1
        return lista1
             