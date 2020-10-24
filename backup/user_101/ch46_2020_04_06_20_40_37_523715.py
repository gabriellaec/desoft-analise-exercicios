def numero_no_indice(l):
    for i, num in enumerate(l):
        if i != num:
            del num
    return l