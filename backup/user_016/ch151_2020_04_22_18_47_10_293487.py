def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    else:
        for i  in range(0,len(lista)-1):
            if lista[i+1] > lista[i]:
                pass
            else:
                break
            if i == len(lista)-2:
                return 'crescente'
        for u in range(0,len(lista)-1):
            if lista[u+1] < lista[u]:
                pass
            else:
                break
            if u == len(lista)-2:
                return 'decrescente'
    return 'nenhum'
