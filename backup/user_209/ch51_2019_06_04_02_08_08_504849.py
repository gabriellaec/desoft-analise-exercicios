def estritamente_crescente (listeras):
    listao = []
    i = 0
    for e in listeras:
        if listeras[e[i+1]] > listeras [e[i]]:
            listao.append(i)
        else:
            continue
        i+=1
    return listao           