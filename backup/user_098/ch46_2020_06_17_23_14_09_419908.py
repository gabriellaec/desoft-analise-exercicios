def numero_no_indice(list):
    list2 = []
    for k, v in enumerate(list):
        if v == k:
            list2.append(k)
    return list2