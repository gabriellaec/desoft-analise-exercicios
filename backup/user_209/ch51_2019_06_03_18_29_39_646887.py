def estritamente_crescente (listeras):
    listao = []
    while i in listeras:
        if listeras[i+1] > listeras [i]:
            listao.append(i)
            i += 1
    return listao           