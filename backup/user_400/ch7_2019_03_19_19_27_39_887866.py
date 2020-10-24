def calcula_norma(lista):
    i = 1
    while i<len(lista):
        lista[0] = lista[0]**2 + lista[1]**2
        lista.remove(lista[1])
        lista[0] = lista[0]**(1/2)
        i += 1
    return int(lista[0])

    

        