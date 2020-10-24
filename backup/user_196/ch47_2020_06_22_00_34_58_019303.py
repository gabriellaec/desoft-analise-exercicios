listafinal = []
def estritamente_crescente(lista):
    for i in range (0, len(lista)):
        if i == 0:
            listafinal.append(lista[i])
        else: 
            if lista[i] > lista[i-1]:
                listafinal.append(lista[i])
    return listafinal
