
def lista_caracteres(x):
    lista = []
    for i in range(0,len(x)):
        if x[i] not in lista:
            lista.append(x[i])
    return lista