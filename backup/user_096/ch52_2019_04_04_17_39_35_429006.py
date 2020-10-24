def eh_crescente(lista):
    i = 1
    listac = []
    if len(lista) == 0:
        return False
    listac.append(lista[0])
    maior = lista[0]
    while i < len(lista):
        if lista[i] >= maior:
            maior = lista[i]
            listac.append(lista[i])
            i+=1
        else:
            i+=1
    if lista == listac:
        return True
    else:
        return False
