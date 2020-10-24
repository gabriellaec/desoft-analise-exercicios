def eh_crescente(lista):
    crescente=False
    i=1
    while i<len(lista):
        if lista[i]>lista[i-1]:
            crescente=True
        i+=1
        return crescente