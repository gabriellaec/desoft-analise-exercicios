def verifica_lista(listanum):
    if len(listanum) == 0:
        return "misturado"
    listapares = []
    listaimpares = []
    for i in range(len(listanum)):
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