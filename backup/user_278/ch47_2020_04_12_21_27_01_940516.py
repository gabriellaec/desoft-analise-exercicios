def estritamente_crescente(l1):
    if l1 == []:
        return l1
    inicial = l1[0]
    l2 = [inicial]
    i = 0
    for i in range (len(l1)-1):
        if l1[i+1] > inicial:
            l2.append(l1[i+1])
    return l2