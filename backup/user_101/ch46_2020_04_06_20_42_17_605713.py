def numero_no_indice(l):
    li = []
    for i, num in enumerate(l):
        if i == num:
            li.append(num)
    return li
