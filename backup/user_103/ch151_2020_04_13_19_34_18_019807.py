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

def estritamente_decrescente(lista2):
    if lista2==[]:
        return []
    i=1
    lista3=[lista2[0]]
    while i < len(lista2):
        if lista2[i]<lista3[len(lista3)-1]:
            lista3.append(lista2[i])
            i+=1
        else:
            i+=1
       
    return lista3

def classifica_lista(lista7):
    if len(lista7)<2:
        return 'nenhum'
    verifica1=estritamente_crescente(lista7)
    verifica2=estritamente_decrescente(lista7)
    if len(verifica1)==len(lista7):
        return 'crescente'
    elif len(verifica2)==len(lista7):
        return 'decrescente'
    else:
        return 'nenhum'
        
    
   