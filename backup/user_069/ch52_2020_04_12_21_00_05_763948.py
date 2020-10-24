def calcula_total_da_nota (p, q):
    p_total = [0]*len(q)
    s = 0
    i = 0
    while i < len(p_total):
        p_total[i] = p[i]*q[i]
        s += p_total[i]
        i += 1
    return s