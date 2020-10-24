def estritamente_decrescente(lista_numeros2):
    if lista_numeros2==[]:
        return []
    x=1
    num2=len(lista_numeros2)
    lista_numeros3=[lista_numeros2[0]]
    while x<num2:
        if lista_numeros2[x]<lista_numeros3[len(lista_numeros3)-1]:
            lista_numeros3.append(lista_numeros2[x])
            x+=1
        else:
            x+=1
    return lista_numeros3

def estritamente_crescente(lista_numeros):
    if lista_numeros==[]:
        return []
    j=1
    lista_numeros1=[lista_numeros[0]]
    num=len(lista_numeros)
    while j<num:
        if lista_numeros[j]>lista_numeros1[len(lista_numeros1)-1]:
            lista_numeros1.append(lista_numeros[j])
            j+=1
        else:
            j+=1
    return lista_numeros1

def classifica_lista(lista_numeros4):
    if len(lista_numeros4)<2:
        return 'nenhum'
    verifica_crescente=estritamente_crescente(lista_numeros4)
    verifica_decrescente=estritamente_decrescente(lista_numeros4)
    if len(verifica_crescente)==len(lista_numeros4):
        return 'crescente'
    elif len(verifica_decrescente)==len(lista_numeros4):
        return 'decrescente'
    else:
        return 'nenhum'