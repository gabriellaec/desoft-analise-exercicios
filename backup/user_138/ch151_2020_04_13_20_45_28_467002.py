def classifica_lista(lista):
    i=0
    while i<len(lista):
        if lista[i]>lista[i+1]:
            return 'decrescente'
        elif lista[i]<lista[i+1]:
            return 'crescente'
        else:
            return 'nenhum'
        i+=1