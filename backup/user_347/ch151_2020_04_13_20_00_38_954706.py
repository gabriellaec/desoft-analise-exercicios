def classifica_lista(lista):
    if lista[0] < lista[-1]:
        return "crescente"
    elif lista[0] > lista[-1]:
        return "decrescente"
    elif range(len(lista)) == 2:
        return "nenhum"
    else:
        return "nenhum"