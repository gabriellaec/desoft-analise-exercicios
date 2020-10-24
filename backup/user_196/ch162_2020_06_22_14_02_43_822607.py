def verifica_lista(listanum):
    if len(lista) == 0:
        return "misturado"
    listapares = []
    listaimpares = []
    for i in range(1, len(listanum)):
        if listanum[i] %2 == 0:
            listapares.append(lista[i])
        elif listanum[i] %2 != 0:
            listaimpares.append(lista[i])     
    if listanum == listapares:
        return "par"
    elif listanum == listaimpares:
        return "ímpar"
    else:
        return "misturado"