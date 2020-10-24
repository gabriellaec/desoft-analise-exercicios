def eh_crescente(lista):
    lista_crescente=[]
    for i in range(len(lista)):
        if lista[i]<lista[i+1]:
            lista_crescente.append(lista[i])
    if lista_crescente=lista:
        return True
    else:
        return False