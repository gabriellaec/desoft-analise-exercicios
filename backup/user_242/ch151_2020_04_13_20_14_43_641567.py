def classifica_lista(lista):
    if lista==[] or len(lista)==1 or lista = [1]:
        return 'nenhum'
    for i in range (len(lista)-1):
        if lista[i+1] <= lista[i]:
            return 'decrescente'
        elif lista[i] < lista[i+1]:
            return 'crescente'
    return lista
    