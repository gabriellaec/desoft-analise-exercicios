def estritamente_crescente (lista1):
    if lista:
        x = [lista1[0]]
        i = 1
        while i < len(lista):
            y = lista1[i]
            if y > x[-1]:
                x.append(y)
        i += 1
        return x
    else:
        return []