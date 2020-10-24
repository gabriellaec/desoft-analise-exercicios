def calcula_fibonacci(n):
    if n == 1:
        return [1]
    elif n == 0:
        return []
    else:
        seq = [1,1]
        i = 1
        while i < n - 1:
            a = seq[i] + seq[i-1]
            seq.append(a)
            i += 1
    return seq