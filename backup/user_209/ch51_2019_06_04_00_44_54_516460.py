def estritamente_crescente (listeras):
    listao = []
    i = 0
    for e in range(listeras):
        if listeras[e[i+1]] > listeras [e[i]]:
            listao.append(i)
        i+=1
    return listao           