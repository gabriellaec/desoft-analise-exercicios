def estritamente_crescente(lista):
    crescente = []
    i = 0
    j = 1
    if len(lista) == 0:
        return crescente
    else:
        crescente.append(lista[i])
        while j < len(lista):
            y=lista[i]
            x=lista[j]
            if y<x:
                crescente.append(x)
                i=j
                j+=1
            else:
                j+=1
        return crescente