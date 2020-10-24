def calcula_total_da_nota(p, q):
    i = 0
    total = 0
    while i < len(p):
        total += p[i] * q[i]
        i += 1
        
    return total