def estritamente_crescente(lista):
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

def eh_crescente(lista2):
    confere=estritamente_crescente(lista2)
    if len(confere)<len(lista2):
        return False
    else:
        return True
        
    

    