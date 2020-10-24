def estritamente_crescente(lista):
    lista=[]
    nova_lista=lista
    i=0
    while i< len(nova_lista):
        if nova_lista[0]>nova_lista[i]:
            del nova_lista[i]
            i+=1
    return nova_lista
   