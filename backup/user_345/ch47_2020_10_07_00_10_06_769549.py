def estritamente_crescente(lista):
    i=0
    z=1
    certa=[]
    if len(lista)>0:
         certa.append(lista[1])
    while z<len(lista):
        if lista[z]>lista[i]:
            certa.append(lista[z])
            i+=1
        z+=1
    return certa