def eh_crescente(lista):
    lista1 = lista
    i = 0
    while i < len(lista1):
        if lista1[i]<lista1[i+1]:
            return True
        else:
            return False
    i+=1