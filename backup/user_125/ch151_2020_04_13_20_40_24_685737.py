def crescente(lista1):
    if lista1==[]:
        return []
    i=1
    lista2=[lista1[0]]
    while i < len(lista1):
        if lista1[i]>lista2[len(lista2)-1]:
            lista1.append(lista1[i])
            i+=1
        else:
            i+=1
    return lista1
def decrescente(lista3):
    if lista3==[]:
        return []
    i=1
    lista4=[lista3[0]]
    while i < len(lista3):
        if lista3[i]<lista4[len(lista4)-1]:
            lista4.append(lista3[i])
            i+=1
        else:
            i+=1
       
    return lista4
def classifica_lista(lista_final):
    if len(lista_final)<2:
        return 'nenhum'
    verificacao=crescente(lista_final)
    verificacao_2=decrescente(lista_final)
    if len(verificacao)==len(lista_final):
        return 'crescente'
    elif len(verificacao_2)==len(lista_final):
        return 'decrescente'
    else:
        return 'nenhum'