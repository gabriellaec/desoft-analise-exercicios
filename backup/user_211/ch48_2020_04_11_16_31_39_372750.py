def eh_crescente(lista):
    j=lista[0]
    for n in lista:
        if n < j:
            return False
        else:
            j=n
        return True
       