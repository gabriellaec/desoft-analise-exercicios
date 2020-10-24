def eh_crescente(lista):
    if lista==[] or len(lista)==1:
        return False
    Maior = lista[0]
    for k in lista:
        if k <= Maior and k != lista[0]:
            return False
    return True

