def eh_crescente(lista):
    i=0
    crescente=True
    while i<(len(lista)-1):
        if lista[i]>=lista[i+1]:
            crescente=False
        i+=1
    return crescente