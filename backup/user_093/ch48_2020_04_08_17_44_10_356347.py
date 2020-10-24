def eh_crescente(lista1):
    i=0
    while i > len(lista1):
        if lista1[i]<=lista1[i+1]:
            return True
        else:
            return False
           