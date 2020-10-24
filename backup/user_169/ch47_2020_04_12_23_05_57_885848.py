def estritamente_crescente(lista):
    if lista==[]:
        return []
    
    maximo=lista[0]
    lista2=[maximo]
    
    if lista!=[]:
        for i in range(len(lista)-1):
            if lista[i+1]> maximo:
                maximo=lista[i+1]
                lista2.append(lista[i+1])


        
    return lista2
