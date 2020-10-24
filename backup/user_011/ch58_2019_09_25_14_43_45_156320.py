def calcula_fibonacci(n):
    seq = [1,1]
    i = 1
    while i < n:
        seq[i+1] = seq[i] + seq[i-1]
        i += 1
    return seq
    