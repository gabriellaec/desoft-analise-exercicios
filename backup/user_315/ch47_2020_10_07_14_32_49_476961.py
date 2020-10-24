def estritamente_crescente(lista):
    crescente = []
    i = 0
    j = 1
    if lista == 0:
        return crescente
    else:
        crescente.append(lista[i])
        while j < len(lista):
            if lista[j] > crescente[i]:
                crescente.append(lista[j])
                i+=1
            j+=1

    return crescente