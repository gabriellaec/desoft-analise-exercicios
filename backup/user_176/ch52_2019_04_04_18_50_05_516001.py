def eh_crescente(lista):
    funcai = True
    i= 1
    while i<len(lista):
        if lista[i] <= lista[i-1]:
            funcao = False
        i += 1
    return True