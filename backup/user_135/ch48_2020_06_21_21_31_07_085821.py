def eh_crescente(lista):
    x = 0
    while x < len(lista) - 1:
        if lista[x] > lista[x+1]:
            verificacao = True
        else:
            verificacao = False
            break
    return verificacao