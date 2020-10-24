def estritamente_crescente (listeras):
    listao = []
    for i in listeras:
        if listeras[i+1] > listeras [i]:
            listao.append(i)
    return listao           