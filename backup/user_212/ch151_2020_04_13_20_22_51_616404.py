def classifica_lista (lista):
    if len(lista) < 2:
        return 'nenhum'
    else: 
        if lista[0]<lista[1] and lista[1]<lista[2] and lista[0]<[:]:
            return 'crescente'
        if lista[0]>lista[1] and lista[1]>lista[2] and lista[0]>[:]:
            return 'decrescente'
        else:
            return 'nenhuma'