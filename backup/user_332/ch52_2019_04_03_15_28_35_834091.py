def eh_crescente (lista):
    if(len(lista) > 1):
        i = 0
        while i < len(lista):
            if(lista[i] > lista[i+1]):
                return False
            i += 1
        return True
