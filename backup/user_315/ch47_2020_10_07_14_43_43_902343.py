def estritamente_crescente(lista):
    crescente = []
    i = 0
    j = 1
    if lista == 0:
        return crescente
    else:
        crescente.append(lista[i])
        while j < len(lista):
            y=lista[i]
            x=lista[j]
            if y<x:
                cresce.append(x)
                i=j
                cj+=1
            else:
                j+=1
        return cresce