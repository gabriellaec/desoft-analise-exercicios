def  eh_crescente(lista):
    i=2
    while i<len(lista):
        if lista[i]>lista[i-1]:
            pass
            if lista[i]==lista[-1]:
                return True
        else:
            return False
            break
        i+=1