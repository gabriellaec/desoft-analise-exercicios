def eh_crescente(lista):
    lista2=[lista[0]]
    i=1
    while i<len(lista):
        if lista[i]>lista[i-1]:
            lista2.append(lista[i])
        else:
            return False
    i+=1