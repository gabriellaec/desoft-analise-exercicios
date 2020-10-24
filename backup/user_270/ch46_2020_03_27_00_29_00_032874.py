def numero_no_indice(list):
    i = 0
    while i < len(list):
        if list[i] != i:
            del list[i]
    i += 1
    return list