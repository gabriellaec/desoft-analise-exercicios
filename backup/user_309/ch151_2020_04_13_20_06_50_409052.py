def classifica_lista(lista):
    if len(lista) == 0:
        return 'nenhum'
    else:
        for i in lista:
            if lista[i-1]<lista[i]:
                return 'crescente'
            if lista[i-1]>lista[i]:
                return 'decrescente'
            else:
                return 'nenhum'