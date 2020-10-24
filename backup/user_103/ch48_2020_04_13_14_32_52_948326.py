def eh_crescente(lista):
    if lista==[]:
        return []
    i=1
    lista1=[lista[0]]
    while i < len(lista):
        if lista[i]>lista1[len(lista1)-1]:
            lista1.append(lista[i])
            i+=1
        else:
            i+=1
    return lista1
    
    j=0
    crescente=True
    while j< len(lista) and crescente:
        if lista[i]!=lista1[i]:
            crescente=False
        j+=1
        return crescente
        
    

    