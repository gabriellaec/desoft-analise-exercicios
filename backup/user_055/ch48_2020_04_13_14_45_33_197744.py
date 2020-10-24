def eh_crescente(lista_crescente):
    if lista_crescente == [] or len(lista_crescente + 1) == 1:
        return True
    for i in range(len(lista_crescente)):
        if lista_crescente[i] >= lista_crescente[i + 1]:
            return False
    return True