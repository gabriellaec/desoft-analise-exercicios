def encontra_maximo(l1):
    listanova = []
    for i in l1:
        for l2 in i:
            listanova.append(abs(l2))
    return max(listanova)
