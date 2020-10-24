def zera_negativos(lista):
    contador=0
    lista2=[]
    i=0
    while contador<len(lista):
        if contador>lista[i]:
            lista2.append(contador)
            
            i+=1
        else:
            lista2.append(lista[i])
    return lista2