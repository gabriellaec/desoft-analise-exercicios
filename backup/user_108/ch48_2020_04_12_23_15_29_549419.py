def eh_crescente(lista):
    for index,n in enumerate(lista):
        if n > lista[index+1]:
            return False
    return True