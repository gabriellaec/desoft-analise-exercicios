def numero_no_indice (lista):
    i=0
    nova_lista =[]
    for e in lista:
        if e == i:
            nova_lista.append (e)
        i +=1
    return nova_lista