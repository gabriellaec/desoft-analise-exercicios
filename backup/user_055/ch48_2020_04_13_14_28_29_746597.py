def eh_crescente(lista_crescente):
    if lista_crescente == [] or len(lista_crescente) == 1:
        return True
    if lista_crescente == sorted(lista_crescente):
        return True
    if lista_crescente[0] == lista_crescente[1]:
        return False
    else:
        return False 