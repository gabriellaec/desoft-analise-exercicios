def calcula_fibonacci (n):
    seq = [0]*n
    seq[0] = 1
    seq[1] = 1
    i = 2 
    while i < n:
        seq[i] = seq[n-1] = seq[n-2]
        i += 1
    return (seq)
        