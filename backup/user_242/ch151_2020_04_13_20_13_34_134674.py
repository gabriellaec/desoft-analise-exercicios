def classifica_lista(lista):
    if lista==[] or len(lista)==1:
        return 'nenhum'
    for i in range (len(lista)-1):
        if lista[i+1] <= lista[i]:
            return 'decrescente'
        else:
            return 'crescente'
    return lista
    