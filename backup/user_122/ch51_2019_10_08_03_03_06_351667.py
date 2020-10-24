def estritamente_crescente(lista):
    i = 0
    nova_lista = []
    #x = 0
    while i <= len(lista):
        if i == 0:
            #x += 1
            nova_lista.append(lista[i])
        elif lista[i] > nova_lista[-1]:
            #x += 1
            nova_lista.append(lista[i])
        i += 1
    return nova_lista