def estritamente_crescente (listeras):
    listao = []
    for i in range(listeras):
        if listeras[i+1] > listeras [i]:
            listao.append(i)
    return listao           