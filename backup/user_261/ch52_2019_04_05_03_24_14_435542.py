def eh_crescente(lista):
    crescente=True
    i=0
    while i<len(lista):
        if lista[i]<lista[i-1]:
            crescente=False
        i+=1
        return crescente