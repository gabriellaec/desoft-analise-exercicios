def eh_crescente(lista):
    for i in range(len(lista)-1):
        if not lista[i+1] > lista[i]:
            return False
    return True