def estritamente_crescente(lista):
    nova_lista=[]
    for i in lista:
        if i[i] > i[i-1]:
            nova_lista.append(i)
        else:
            del (i)
            