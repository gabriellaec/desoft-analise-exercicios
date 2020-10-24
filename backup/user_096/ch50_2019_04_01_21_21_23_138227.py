lista = [0,1,3,3,2,5]
def numero_no_indice(lista):
    listaa = []    
    for i in range(len(lista)):
        if i == lista[i]:
            listaa.append(lista[i])
    return listaa