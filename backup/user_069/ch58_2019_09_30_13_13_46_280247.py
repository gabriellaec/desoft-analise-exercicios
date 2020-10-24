def calcula_fibonacci (n):
    seq = [0]*n
    i = 0 
    while i < n:
        seq[i] = seq[n-1] + seq[n-2]
        i += 1
    return (seq)
        