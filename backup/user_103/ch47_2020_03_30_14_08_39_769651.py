def estritamente_crescente(lista):
    i=len(lista)
    while lista[0]<lista[i]:
        if lista[i-1]<lista[i]:
            lista2=lista[i]
        return lista2