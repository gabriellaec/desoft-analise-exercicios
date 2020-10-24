def separa_trios(lista):
    lista1=[]
    i=0
    while i<len(lista):
        lista1.append(lista[i:i+2])
        i+=1
        return lista1
             