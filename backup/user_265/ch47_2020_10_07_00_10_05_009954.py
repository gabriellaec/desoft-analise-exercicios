def estritamente_crescente(lista):
    certa = []
    i = 0
    z = 1
    if i < len(lista):
        certa.append(lista[i])

    while z < len(lista):
        if  lista[z] > certa[i]:
            certa.append(lista[z])
            i += 1
        z += 1
        
    return certa
    