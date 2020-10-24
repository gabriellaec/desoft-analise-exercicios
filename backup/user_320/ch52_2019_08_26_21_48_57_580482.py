def eh_crescente(lista):
    ant = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < ant:
            return False
        ant = lista[i]
    return True