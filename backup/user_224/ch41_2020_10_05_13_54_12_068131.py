nova_lista = []

def zera_negativos(lista) :
    i = 0
    while i < len(lista) :
        if lista[i] < 0 :
            lista[i] = 0
        else :
            lista[i] = lista[i]
        s = nova_lista.append(lista[i])
        i += 1
    return s
