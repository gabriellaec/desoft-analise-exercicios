def estritamente_crescente(lista):
    if lista== []:
        return []
    lista_estritamente_crescente= []
    lista_estritamente_crescente.append(lista[0])
    maximo= lista[0]
    i= 0
    while i < len(lista):
        if lista[i] > maximo:
            maximo=lista[i]
            i= i + 1
        else:
            i= i + 1
    if lista_estritamente_crescente==lista:
        return True
    else:
        return False
    