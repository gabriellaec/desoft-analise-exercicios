def classifica_lista(lista):
    if len(lista) < 2:
        return ("nenhum")
    else:
        if lista[0] > lista[1]:
            for i in range(2, len(lista)):
                if lista[i] > lista[i-1]:
                    return ("nenhum")
            return ("decrescente")
        else:
            for i in range(2, len(lista)):
                if lista[i] < lista[i-1]:
                    return ("nenhum")
            return ("crescente")