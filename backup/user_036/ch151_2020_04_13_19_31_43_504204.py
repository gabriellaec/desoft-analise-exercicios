def classifica_lista(lista):
    for i in range(len(lista)-1):
        if lista[i+1] < lista[i]:
            return 'decrescente'
        elif lista[i+1] == lista[i]:
            return 'nenhum'
        else:
            return 'crescente'