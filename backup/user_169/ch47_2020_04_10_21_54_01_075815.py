def estritamente_crescente(lista):
    if lista:
        lista2=[lista[0]]
        i=0
        while i <len(lista):
            if lista[i]>lista2[-1]:
                lista2.append(lista)
            i+=1
    return lista2
    
    else:
        return []


    
