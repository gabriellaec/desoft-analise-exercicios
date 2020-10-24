def junta_nomes(l0,l1,l2):
    result = []
    for i in l0:
        for e in l2:
            result.append(i + " " + e)
    for a in l1:
        for b in l2:
            result.append(a + " " + b)
    return result