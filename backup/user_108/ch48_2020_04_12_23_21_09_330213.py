def eh_crescente(lista):
    print(lista)
    for index,n in enumerate(lista[1:]):
        if n <= lista[index-2]:
            return False
    return True