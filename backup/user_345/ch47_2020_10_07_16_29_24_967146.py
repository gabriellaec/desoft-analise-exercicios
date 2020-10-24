def estritamente_crescente(lista):
    i=0
    z=1
    certa=[]
    if i < len(lista):
        certa.append(lista[i])
    while z < len(lista):
        if lista[z]>lista[i]:
            certa.append(lista[z])
            i+=1
        z+=1
    return certa