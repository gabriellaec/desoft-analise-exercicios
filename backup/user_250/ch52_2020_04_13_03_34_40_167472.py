def calcula_total_da_nota(p,q):
    tot = 0
    for i in range(len(p)-1):
        x = p[i]*q[i]
        tot = tot+x
    return tot