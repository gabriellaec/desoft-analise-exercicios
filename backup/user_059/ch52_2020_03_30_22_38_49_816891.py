def calcula_total_da_nota(l1, l2):
    x = [0]*len(l1)
    i=0
    while i<len(l1):
        x[i] = l1[i]*l2[i]
        i+=1
    return sum(x)
