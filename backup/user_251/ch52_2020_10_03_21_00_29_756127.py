def calcula_total_da_nota(p, q):
    item = 0
    total = 0
    while i < len(p):
        total += p[i] * q[i]
        item += 1
        
    return total