def classifica_lista (lista):
    i=0
    if len(lista) < 2:
        return 'nenhum'

    while i < len(lista):
        
        if lista[i+1]>lista[i]:
            return 'crescente'

        elif lista[i+1]<lista[i]:
            return 'decrescente'

        elif lista[i+1] == lista[i] or lista[i+1] != lista[i]:
            return 'nenhum'
        
        else:
            return 'decrescente'
        i+=1