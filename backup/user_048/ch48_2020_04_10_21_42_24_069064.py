def  eh_crescente(lista):
    i=1
    while i<len(lista):
        if len(lista)==0:
            return True
        elif lista[i]>lista[i-1]:
            pass
            if lista[i]==lista[-1]:
                return True
        else:
            return False
            break
        i+=1