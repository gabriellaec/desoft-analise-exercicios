def estritamente_crescente (lista):
    if lista == []:
        return ([])
    else:
        inicial=lista[0]
        crescendo=[inicial]
        for i in range (0,len(lista)-1):
            if lista[i+1] > inicial:
                inicial=lista[i+1]
                crescendo.append(inicial)
    return crescendo
                