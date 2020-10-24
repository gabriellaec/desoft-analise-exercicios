def eh_crescente(lista):
    i = 0
    z = 1
    while z < len(lista):
        if not lista[z] > lista[i]:
            return False
        else:
            return True
        i += 1
        z += 1