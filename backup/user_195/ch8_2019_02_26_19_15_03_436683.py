def verifica_progressao(L):
    if L[1]/L[0]==L[1]-L[0]:
        return ("AG")
    elif L[1]/L[0]==L[2]/L[1]:
        return ("PG")
    elif L[1]-L[0]==L[2]-L[1]:
        return ("PA")
    else:
        return ("NA")
    
print (verifica_progressao(L))