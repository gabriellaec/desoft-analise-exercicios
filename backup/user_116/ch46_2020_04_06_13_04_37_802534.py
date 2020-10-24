def numero_no_indice(lista):
    i=0
    lista3=[]
    while i < len(lista):
        if i == lista[i]:
            lista3.append(lista[i])
            i+=1
        else:
            i+=1
    return lista3
    
