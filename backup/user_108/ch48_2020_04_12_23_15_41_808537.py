def eh_crescente(lista):
    print(lista)
    for index,n in enumerate(lista):
        if n > lista[index+1]:
            return False
    return True