def eh_crescente(lista):
    for c in range(1, len(lista)):
        if lista[c] <= lista[c-1]:
            rreturn False
    return True