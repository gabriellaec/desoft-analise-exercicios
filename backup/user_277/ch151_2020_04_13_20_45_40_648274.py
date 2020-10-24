def classifica_lista(lista):
    if len(lista)<2:
        return 'nenhum'
    #definindo lista decrescente
    lista_decrescente=[]
    lista_decrescente=[lista[0]]
    q=1
    f=0
    while q<len(lista):
        if lista[q]<lista_decrescente[f]:
            lista_decrescente.append(lista[q])
            k+=1
        e+=1
        
    #definindo lista crescente
    lista_crescente=[]
    lista_crescente=[lista[0]]
    j=1
    e=0
    while j<len(lista):
        if lista[j]>lista_crescente[e]:
            lista_crescente.append(lista[j])
            e+=1
        j+=1
    #finalizando lista
    if lista_decrescente==lista:
        return 'decrescente'
    elif lista_crescente==lista:
        return 'crescente'
    else:
        return 'nenhum'