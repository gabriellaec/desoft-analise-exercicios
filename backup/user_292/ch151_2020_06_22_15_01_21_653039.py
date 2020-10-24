def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    c = 0
    e = 0
    for i in range(len(lista)-1):
        if lista[i+1]>lista[i]:
            c +=1
        else:
            e += 1
    if len(lista) == c:
        return 'crescente'
    c = 0
    e = 0
    for i in range(len(lista)-1):
        if lista[i+1] < lista[i]:
            c+=1
        else:
            e+=1
    if len(lista) == c:
        return 'decrescente'
    else:
        return 'nenhum'
