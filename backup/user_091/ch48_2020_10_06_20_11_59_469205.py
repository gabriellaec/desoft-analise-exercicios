def eh_crescente(lista):
    if lista== []:
        return False
    if len(lista)==1:
        return False
    lista_estritamente_crescente= []
    lista_estritamente_crescente.append(lista[0])
    maximo= lista[0]
    i= 0
    while i < len(lista):
        if lista[i] > maximo:
            maximo=lista[i]
            lista_estritamente_crescente.append(lista[i])
            i= i + 1
        else:
            i= i + 1
    if len(lista)==len(lista_estritamente_crescente):
        return True
    else:
        return False
    