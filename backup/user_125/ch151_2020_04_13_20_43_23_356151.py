def crescente(lista_inicial):
    if lista_inicial==[]:
        return []
    i=1
    lista2=[lista[0]]
    while i < len(lista_inicial):
        if lista_inicial[i]>lista2[len(lista2)-1]:
            lista2.append(lista_inicial[i])
            i+=1
        else:
            i+=1
       
    return lista2

 

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
    if len(list_final)<2:
        return 'nenhum'
    verifica=crescente(lista_final)
    verifica2=decrescente(lista_final)
    if len(verifica)==len(lista_final):
        return 'crescente'
    elif len(verifica2)==len(lista_final):
        return 'decrescente'
    else:
        return 'nenhum'