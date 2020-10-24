def separa_trios (lista):
    nova = []
    i = 0
    j = 3
    while i < len(lista):
        nova.append(lista[i:j])
        i += 3
        j += 3
    return nova