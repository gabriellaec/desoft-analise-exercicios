def estritamente_crescente(lista):
    lista2=[]
    for i in range(len(lista)):
        if i not in lista2:
            lista2.append(lista[i])
    x=sorted(lista2)
    return x