def estritamente_crescente(lista):
    crescente = []
    if len(lista) == 0:
        return crescente
    else:
        crescente.append(lista[0])
        i = 1
        while i<len(lista):
            if lista[i]>lista[i-1]:
                crescente.append(lista[i])
                i+=1
            else:
                break
    return crescente
print(estritamente_crescente([1, 2, 3, 2, 5, 6]))