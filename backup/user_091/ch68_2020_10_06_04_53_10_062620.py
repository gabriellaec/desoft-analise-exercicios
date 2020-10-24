def separa_trios(lista):
    lista1=[]
    i=0
    while i<len(lista):
        lista1.append(lista[i:i+3])
        i+=1
        return lista1
             