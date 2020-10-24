def  eh_crescente(lista):
    i=1
    if len(lista)<2:
        return True
    else:
        while i<len(lista):
            if lista[i]>lista[i-1]:
                pass
                if lista[i]==lista[-1]:
                    return True
            else:
                return False
                break
            i+=1