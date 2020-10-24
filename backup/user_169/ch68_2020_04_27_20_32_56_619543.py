def separa_trios(lista):
    
    lista2=[]
    for i in range(len(lista)):
        if len(lista)>2:
            lista2.append(lista[i:i+3:3])
        
        elif len(lista)>1:
            lista2.append(lista[i:i+2])

        else:
            lista2.append(lista[i])

    return lista2