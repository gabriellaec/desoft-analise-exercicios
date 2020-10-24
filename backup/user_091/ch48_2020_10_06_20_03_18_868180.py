def eh_crescente(lista):
    if lista== []:
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
    verifica=0
    g=0
    while g<len(lista):
        if len(lista)==len(lista_estritamente_crescente):
            verifica+=1
            g+=1
        else:
            g+=1
    if verifica==len(lista):
        return True
    else:
        return False
    