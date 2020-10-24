nova_lista = []
i = 0
def zera_negativos(lista) :
    while i < len(lista) :
        if lista[i] < 0 :
            lista[i] = 0
        i += 1
        s = nova_lista.append(lista[i])     
    return s
