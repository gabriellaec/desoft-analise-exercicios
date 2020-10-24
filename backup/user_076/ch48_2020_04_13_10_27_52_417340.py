def eh_crescente (lista):
    i=0
    while i < len(lista):
        if lista[i] < lista[i+1]:
            crescente = True
        elif lista[i]<lista[i+1]:
            crescente = False
            continue
        i+=1
    return crescente
        