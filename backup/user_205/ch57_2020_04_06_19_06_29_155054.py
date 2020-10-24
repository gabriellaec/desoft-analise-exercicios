def verifica_progressao(lista):
    for numeros in lista:
        if (lista[0]+lista[2])/2 == lista[1]:
            return ("PA")
        elif (lista[1]**2 == lista[0]*lista[2]):
            return ("PG")
        elif ((lista[0]+lista[2])/2 == lista[1] and lista[1]**2 == lista[0]*lista[2]):
            return ("AG")
        else:
            return ("NA")