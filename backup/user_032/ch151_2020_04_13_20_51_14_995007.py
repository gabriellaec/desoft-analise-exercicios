def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    else:
        i = 0
        while i < len(lista):
            for i in lista:
                if lista[i+1] < lista [i]:
                    return "decrescente"
                elif lista[i+1] > lista[i]:
                    return "crescente"
                else:
                    return 'nenhum'
                i=i+1