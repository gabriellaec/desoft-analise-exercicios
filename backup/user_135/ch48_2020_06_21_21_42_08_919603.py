def eh_crescente(lista):
    x = 0
    while len(lista) - 1 > x:
        if lista[x] > lista[x+1]:
            verificacao = False
            break
        else:
            verificacao = True
    return verificacao