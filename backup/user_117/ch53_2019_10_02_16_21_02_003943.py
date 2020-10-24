l2 = []
def inverte_lista(l1):
    i = 0
    while i < len(l1):
        l2.append(l1[::-1])
        i+=1
    return l2