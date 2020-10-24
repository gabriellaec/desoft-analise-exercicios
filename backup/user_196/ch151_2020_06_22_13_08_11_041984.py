def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    for i in range(1, len(lista)):
        if lista[i] > lista[i-1]:
            return "crescente"
        elif lista[i] < lista [i-1]:
            return "decrescente"
        else:
            return "nenhum"
