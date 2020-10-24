def classifica_lista(lista):
    i = 0
    while i < len(lista):
        if lista[i+1] > lista[i]:
            return 'crescente'
        elif lista[i+1] < lista[i]:
            return 'decrescente'
        elif 0<= len(lista) < 2:
            return 'nenhum'
        else:
            return 'nenhum'
        i += 1