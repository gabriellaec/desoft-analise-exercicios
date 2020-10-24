def junta_nome_sobrenome(l1, l2):
    lf = [0]*len(l1)
    i = 0
    while i<len(l1):
        lf[i] = ('{} {}'.format(l1[i], l2[i]))
    return lf