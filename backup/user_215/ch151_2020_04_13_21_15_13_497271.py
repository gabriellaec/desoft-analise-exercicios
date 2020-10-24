def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    result = lista[1] - lista[0]
    if result > 0:
        for i in range(len(lista)-1):
            if lista[i+1] - lista[i] <= 0:
                return "nenhum"
    if result < 0:
        for i in range(len(lista)-1):
            if lista[i+1]-lista[i] >= 0:
                return "nenhum"
    if result == 0:
        return "nenhum"
    elif result > 0:
        return "crescente"
    elif result < 0:
        return "decrescente"