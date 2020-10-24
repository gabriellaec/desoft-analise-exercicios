def verifica_progressao(L):
    if len(L)<=2 or L[1]/L[0]==L[2]/L[1] and L[1]-L[0]==L[2]-L[1]:
        return ("AG")
    elif L[1]/L[0]==L[2]/L[1]:
        return ("PG")
    elif L[1]-L[0]==L[2]-L[1]:
        return ("PA")
    else:
        return ("NA")
L=[1,4,7]
print (verifica_progressao(L))
