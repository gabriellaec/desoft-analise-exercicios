def estritamente_crescente (lista):
    if lista:
        leo = [lista[0]]
        i = 1
        while i < len(lista):
            jota = lista[i]
            if jota > leo[-1]:
                leo.append(jota)
            i += 1
        return leo
    else:
        return []
                          
            