
def calcula_norma(a):
    lista = a
    i = 0
    o = 1
    while o<len(lista):
        lista[0] = lista[0]**2 + lista[1]**2
        lista.remove(lista[1])
        lista[0] = lista[0]**(1/2)
        o += 1
    return lista[0]

    

        