def classifica_lista(lista):
    count = 0
    
    for i in range(len(lista)):
        if lista[i] != count:
            count = lista[i]
        else:
            return 'nenhum'
   
    if len(lista) < 2 or (lista != sorted(lista, key=int) and lista != sorted(lista, key=int, reverse=True)):
        return 'nenhum'
    else:
        if lista != sorted(lista, key=int):
            return 'decrescente'
        elif lista == sorted(lista, key=int):
            return 'crescente'