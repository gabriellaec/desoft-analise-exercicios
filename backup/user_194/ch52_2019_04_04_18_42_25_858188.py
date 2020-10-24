def eh_crescente(lista):
    funcao = True
    i = 0
    while i < len(lista):
        if lista[i] > lista[i-1]:
            funcao = True
        else:
            funcao = False
    i += 1
    return funcao