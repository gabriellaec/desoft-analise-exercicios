def eh_crescente(lista):
    j=lista[0]
    lista2=[j]
    i=0
    while i < (len(lista)-1):
        if lista[i]>j:
            j=lista[i]
            lista2.append(lista[i])
    if lista==lista2:
        return True
    else:
        return False 