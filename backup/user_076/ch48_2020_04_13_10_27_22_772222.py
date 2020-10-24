def eh_crescente (lista):
    i=0
    while i < len(lista):
        if lista[i] < lista[i+1]:
            crescente = True
            i+=1
        elif lista[i]<lista[i+1]:
            crescente = False
            break
    return crescente
        