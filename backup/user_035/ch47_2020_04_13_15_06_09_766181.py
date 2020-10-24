def estritamente_crescente(l1):
    if l1 == []:
        return l1
    else:
        inicial = l1[0]
        l2 = [inicial]
        for i in range(len(l1)-1):
            if l1[i+1]>inicial:
                inicial = l1[i+1]
                l2.append(l1(i+1))
        return l2